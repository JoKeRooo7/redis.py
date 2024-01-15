# pip3 install ansible
# ansible-playbook deploy.yml
# /Users/lynseypi/Library/Python/3.7/bin/ansible-playbook deploy.yml

import yaml

IMPORT_YAML = "../materials/todo.yml"

with open(IMPORT_YAML, "r") as todo_file:
    import_data = yaml.safe_load(todo_file)

# развернуть сервер
ansible_task = [{
    "hosts": "localhost",
    "tasks": []
}]

ansible_task[0]["tasks"].append({
    "name": "Install packeges",
    "apt": {
        "name": import_data["server"]["install_packages"]
    }
})

# arg_one = "./" + "".join(import_data["server"]["exploit_files"][1])
arg_two = "./" + "".join(import_data["server"]["exploit_files"][0])
arg_add = "./server_data.py"

args = " " + "".join(import_data["server"]["exploit_files"][1])

ansible_task[0]["tasks"].append({
    "name": "Run produser",
    "command": "python3" + args,
})

args = " -e " + ",".join(import_data["bad_guys"])
args = " " + "".join(import_data["server"]["exploit_files"][0]) + args

ansible_task[0]["tasks"].append({
    "name": "Run consumer",
    "command": "python3" + args,
})


ansible_yaml = yaml.dump(ansible_task, default_flow_style=False,
                         explicit_start=True, indent=2,
                         sort_keys=False, default_style=False)

with open("deploy.yml", "w") as deploy_file:
    deploy_file.write(ansible_yaml)
