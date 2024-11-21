#!/usr/bin/env python3

import subprocess
import json
import requests
import argparse

uri = "https://magin.onara.top"

def fetch_package(pkg):

    try:
        local_url = f"{uri}/p/{pkg}.json"
        print(local_url)
        response = requests.get(local_url)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error al descargar el json: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error al decodificar el json: {e}")
        return None

def run(r):
    print(f"Executing: {r}")
    subprocess.run(r, shell=True)


def install(pkg_name):
    pkg = fetch_package(pkg_name)

    try:
        run(" && ".join(pkg["run"]))
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")
    
def main():
    parser = argparse.ArgumentParser(description="Magin Package Manager")
    subparsers = parser.add_subparsers(dest="command")

    install_parser = subparsers.add_parser("install")
    install_parser.add_argument("package", type=str)
    
    args = parser.parse_args()

    if args.command == "install":
        install(args.package)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
