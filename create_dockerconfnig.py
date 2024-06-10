import base64
import json

def encode_to_base64(data):
    """Encode a string to base64."""
    return base64.b64encode(data.encode()).decode()

def generate_dockerconfig_json(username, token):
    """Generate the .dockerconfigjson content."""
    auth_string = f"{username}:{token}"
    encoded_auth = encode_to_base64(auth_string)

    dockerconfig = {
        "auths": {
            "ghcr.io": {
                "auth": encoded_auth
            }
        }
    }
    
    dockerconfig_json = json.dumps(dockerconfig)
    encoded_dockerconfig_json = encode_to_base64(dockerconfig_json)

    return encoded_dockerconfig_json

def create_dockerconfig_yml(encoded_dockerconfig_json):
    """Create the final YAML content."""
    yml_content = f"""
kind: Secret
type: kubernetes.io/dockerconfigjson
apiVersion: v1
metadata:
  name: dockerconfigjson-github-com
  labels:
    app: app-name
data:
  .dockerconfigjson: {encoded_dockerconfig_json}
"""
    return yml_content

def main():
    # Get GitHub username and token from user
    github_username = input("Enter your GitHub username: ")
    github_token = input("Enter your GitHub token: ")

    # Generate the encoded .dockerconfigjson content
    encoded_dockerconfig_json = generate_dockerconfig_json(github_username, github_token)

    # Create the final YAML content
    dockerconfig_yml = create_dockerconfig_yml(encoded_dockerconfig_json)

    # Write the YAML content to a file
    with open('dockerconfig.yml', 'w') as f:
        f.write(dockerconfig_yml)

    print("dockerconfig.yml has been created successfully.")

if __name__ == "__main__":
    main()
