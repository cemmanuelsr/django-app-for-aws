# Projeto Final - Matéria de Redes de Computadores e Cloud

Este projeto tem como objetivo implementarmos a arquitetura proposta em classe na **AWS**, utilizando **Terraform** para isso e então fazermos deploy nessa de um aplicativo Django simples, usando **Ansible** para isso. E, no meu caso, é o CRUD para um sistema de notas simples.

## Setup

Para seguir os passos do projeto, é necessário ter instalado na máquina o [Terraform](https://www.terraform.io/), o [Ansible](https://www.ansible.com/), o kubectl e o awscli. Além de docker caso queira editar a imagem do Django que está sendo lançada.

## Arquitetura

Aqui vamos falar sobre as partes mais importantes, isso significa que detalhes sobre o aplicativo django serão omitidos, já que o foco não é desenvolver uma aplicação, mas fazer deploy de uma. Também é necessário ter configuradas as variáveis de ambiente localmente.

### terraform

Na pasta terraform é possível ver o arquivo [main.tf](https://raw.githubusercontent.com/cemmanuelsr/django-app-for-aws/master/terraform/main.tf). Nele está as configurações sobre a arquitetura da solução como:

- Subredes;
- Módulo VPC;
- Módulo EKS;
- Tipo da instância, número de instâncias, etc...


### ansible

Nessa pasta estão os arquivos para implementar o metrics-server em nosso cluster em [components.yaml](https://raw.githubusercontent.com/cemmanuelsr/django-app-for-aws/master/ansible/components.yaml). Estamos usando uma versão local pois foi preciso adicionar ao script original provido pela AWS a tag `hostNetwork: true`.

Para implementar o metrics-server basta seguir os passos na [documentação oficial da AWS](https://docs.aws.amazon.com/eks/latest/userguide/metrics-server.html).

Nessa pasta também está o arquivo [app.yml](https://raw.githubusercontent.com/cemmanuelsr/django-app-for-aws/master/ansible/app.yml), responsável por configurar o container da nossa aplicação.

E por último, o [playbook.yml](https://raw.githubusercontent.com/cemmanuelsr/django-app-for-aws/master/ansible/playbook.yml) que realiza o deploy da aplicação como especificada em `app.yml` e implementa o horizontal autoscale como especificado na [documentação da AWS](https://docs.aws.amazon.com/eks/latest/userguide/horizontal-pod-autoscaler.html).
