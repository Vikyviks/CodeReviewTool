users = {
    "admin": {"password": "securepassword", "role": "admin"},
    "dev": {"password": "devpassword", "role": "developer"}
}

def authenticate(username, password):
    user = users.get(username)
    if user and user["password"] == password:
        return {"username": username, "role": user["role"]}
    return None

if __name__ == "__main__":
    print(authenticate("admin", "securepassword"))

