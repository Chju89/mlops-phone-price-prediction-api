# 🛠️ Ansible - Jenkins & Docker Setup

Thư mục này chứa Ansible playbook để:

- Cài Docker
- Cài Jenkins
- Cài các công cụ CLI cần thiết: kubectl, helm, black, pytest, ruff

## Cấu trúc
```
ansible/
├── inventory.ini
├── playbook.yml
└── roles/
    ├── docker/
    │   └── tasks/main.yml
    └── jenkins/
        └── tasks/main.yml
```

## Cách chạy
```bash
ansible-playbook -i inventory.ini playbook.yml
```
