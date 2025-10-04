import yaml
import subprocess
from copy import deepcopy
from colorama import Fore, Style, init

init(autoreset=True)

BASE_FILE = "docker-compose.base.yml"
OUTPUT_FILE = "docker-compose-selected.yml"


def print_banner():
    print(f"\n{Fore.CYAN}{'='*50}")
    print(f"{Fore.GREEN}{Style.BRIGHT}        🚀 Proyecto InitOps - Docker Manager")
    print(f"{Fore.CYAN}{'='*50}\n")


def load_base_compose():
    with open(BASE_FILE, "r") as f:
        return yaml.safe_load(f)


def select_services(services):
    print(f"{Fore.YELLOW}Seleccione los servicios que desea levantar:")
    for i, s in enumerate(services, start=1):
        print(f"  {Fore.CYAN}{i}. {Fore.WHITE}{s}")
    print()
    selected = input(
        f"{Fore.GREEN}Ingrese números separados por coma: {Fore.WHITE}"
    ).split(",")
    selected = [services[int(i.strip()) - 1] for i in selected if i.strip().isdigit()]
    print(f"\n{Fore.GREEN}✅ Servicios seleccionados: {', '.join(selected)}\n")
    return selected


def generate_compose(base, selected):
    new_compose = deepcopy(base)
    new_compose["services"] = {
        k: v for k, v in base["services"].items() if k in selected
    }

    if "volumes" in base:
        new_compose["volumes"] = {k: None for k in base["volumes"].keys()}

    yaml_dump = yaml.dump(new_compose, default_flow_style=False, sort_keys=False)
    yaml_dump = yaml_dump.replace(": null", ":")

    with open(OUTPUT_FILE, "w") as f:
        f.write(yaml_dump)

    print(f"{Fore.CYAN}✅ Archivo {OUTPUT_FILE} generado correctamente.\n")


def run_docker_compose():
    print(f"{Fore.MAGENTA}▶ Ejecutando docker compose up -d...\n")
    cmd = ["docker", "compose", "-f", OUTPUT_FILE, "up", "-d"]
    subprocess.run(cmd)
    print(f"\n{Fore.GREEN}🚀 Contenedores levantados correctamente.\n")


def main():
    print_banner()
    base = load_base_compose()
    services = list(base["services"].keys())
    selected = select_services(services)
    generate_compose(base, selected)

    run = input(
        f"{Fore.YELLOW}¿Desea ejecutar 'docker compose up -d'? (s/n): {Fore.WHITE}"
    ).lower()
    if run == "s":
        run_docker_compose()
    else:
        print(
            f"{Fore.BLUE}👌 Puede ejecutar manualmente: docker compose -f {OUTPUT_FILE} up -d\n"
        )


if __name__ == "__main__":
    main()
