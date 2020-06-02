terraform init
terraform refresh -state-out=my-state.tfstate
terraform plan -out=my-state.plan
terraform show --json my-state.plan | jq -r '.planned_values.root_module.resources' > temp-state.json
python3 converge_tf_state.py temp-state.json.json my-stat.tfstate
