# ⚙️ Ansible Setup for Jenkins CI/CD VM (GCP)

This Ansible playbook automates the installation of **Docker** and **Jenkins** on a Google Compute Engine (GCE) VM running Ubuntu 22.04. This VM acts as the CI/CD server for the MLOps pipeline.

---

## 📦 Features

- ✅ Installs Docker and adds user to the `docker` group
- ✅ Installs Jenkins and starts the service
- ✅ Sets up everything via SSH using `inventory.ini`
- ✅ Compatible with GCP VM provisioned by Terraform

---

## 📁 Folder Structure

```
ansible/
├── inventory.ini          # GCP VM public IP and SSH user
├── playbook.yml           # Main playbook
└── roles/
    ├── docker/
    │   └── tasks/main.yml
    └── jenkins/
        └── tasks/main.yml
```

---

## 🚀 How to Use

### 1. SSH Access Configuration

Update `inventory.ini` with your VM's external IP and SSH user:

```ini
[jenkins]
34.170.133.145 ansible_user=YOUR_VM_USER ansible_ssh_private_key_file=~/.ssh/id_rsa
```

> Replace `YOUR_VM_USER` with the actual username (e.g. `trieu-nguyen`).
> Ensure your SSH key is valid and can access the VM.

---

### 2. Run the Playbook

```bash
cd ansible
ansible-playbook -i inventory.ini playbook.yml
```

---

## 🔍 Verify Setup

- Jenkins: `http://<EXTERNAL_IP>:8080`
- Get Jenkins setup password:

```bash
sudo cat /var/lib/jenkins/secrets/initialAdminPassword
```

- Check Docker installation:

```bash
docker ps
```

> Re-login after the playbook to ensure your user is in the `docker` group.

---

## 🧩 Dependencies

- Ubuntu 22.04 on the VM
- Ansible installed on local machine:
```bash
pip install ansible
```

---

## 📌 Notes

- This playbook is part of a complete [MLOps pipeline project](https://github.com/Chju89/mlops-phone-price-prediction-api).
- Infrastructure (VM, GKE, GCS, etc.) is provisioned using Terraform.

---

## 📧 Author

Quangtrieu Nguyen – for MLOps job portfolio  
[GitHub Repo](https://github.com/Chju89/mlops-phone-price-prediction-api)
