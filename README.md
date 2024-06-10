# MizSIM for Nautilus

1. create a secret:
* kubectl create -f dockerconfig.yml

* run python create_dockerconfig.py if you need to create a secret file

2. create a workspace:
* kubectl create -f ue-workspace.yml

3. run the pod:
* kubectl create -f podUnreal.yml