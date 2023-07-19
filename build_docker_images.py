import os
import subprocess

def build_docker_images(path):
    for child in os.listdir(path):
        child_path = os.path.join(path, child)
        if os.path.isdir(child_path):
            print(child_path)
            if "Dockerfile" in os.listdir(child_path):
                image_name = os.path.basename(child_path)
                print(f"Building Docker image: {image_name}")
                process = subprocess.run(["docker", "build", "-t", image_name, child_path])
                if process.returncode != 0:
                    print(f"Error building Docker image: {image_name}")

if __name__ == "__main__":
    current_directory = os.path.dirname(os.path.realpath(__file__))
    build_docker_images(current_directory)