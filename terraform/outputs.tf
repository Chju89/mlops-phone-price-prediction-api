output "jenkins_vm_ip" {
  value = google_compute_instance.jenkins.network_interface[0].access_config[0].nat_ip
}

output "gke_cluster_name" {
  value = google_container_cluster.mlops_cluster.name
}

output "artifact_registry_repo" {
  value = google_artifact_registry_repository.repo.repository_id
}

output "bucket_name" {
  value = google_storage_bucket.mlflow_bucket.name
}

