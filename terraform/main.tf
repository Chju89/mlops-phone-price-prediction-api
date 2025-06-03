# GCS Bucket
resource "google_storage_bucket" "mlflow_bucket" {
  name     = "${var.project_id}-mlflow-bucket"
  location = var.region
}

# Artifact Registry
resource "google_artifact_registry_repository" "repo" {
  provider      = google
  location      = var.region
  repository_id = "mlops-repo"
  format        = "DOCKER"
  description   = "Artifact Registry for MLOps images"
}

# GKE Cluster
resource "google_container_cluster" "mlops_cluster" {
  name     = "mlops-cluster"
  location = var.region

  remove_default_node_pool = true
  initial_node_count       = 1
  deletion_protection = false
}

resource "google_container_node_pool" "primary_nodes" {
  cluster    = google_container_cluster.mlops_cluster.name
  location   = var.region
  name       = "primary-node-pool"

  node_config {
    machine_type = "e2-medium"
    disk_size_gb = 30
    oauth_scopes = [
      "https://www.googleapis.com/auth/cloud-platform"
    ]
  }

  initial_node_count = 1
}

# Jenkins VM (e2-micro, Ubuntu)
resource "google_compute_instance" "jenkins" {
  name         = "jenkins-vm"
  machine_type = "e2-micro"
  zone         = var.zone

  boot_disk {
    initialize_params {
      image  = "projects/ubuntu-os-cloud/global/images/family/ubuntu-2004-lts"
      size   = 20
    }
  }

  network_interface {
    network = "default"
    access_config {}
  }

  metadata_startup_script = file("${path.module}/scripts/install_jenkins.sh")
}

# Firewall Rule for Jenkins (8080) & MLflow (5000)
resource "google_compute_firewall" "allow_custom_ports" {
  name    = "allow-jenkins-mlflow"
  network = "default"

  allow {
    protocol = "tcp"
    ports    = ["8080", "5000"]
  }

  source_ranges = ["0.0.0.0/0"]
  target_tags   = ["jenkins"]
}

