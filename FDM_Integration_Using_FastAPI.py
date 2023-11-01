from fastapi import FastAPI
import requests

app = FastAPI()
USERNAME = "admin"
PASSWORD = "Sbxftd1234!"


def get_token():
    # Code to obtain the token from FDM
    url = f"https://10.10.20.65/api/fdm/latest/fdm/token"
    payload = {
        "grant_type": "password",
        "username": USERNAME,
        "password": PASSWORD,
        "expires_in": 31536000
    }
    headers = {
        "Content-Type": "application/json",
    }
    response = requests.post(url, headers=headers, json=payload, verify=False)
    if response.status_code == 200:
        token = response.json().get("access_token")
        return token
    else:
        raise Exception("Failed to obtain FDM token")


@app.get("/get-token")
def retrieve_token():
    token = get_token()
    if token:
        # Use the token here
        return {"token": token}
    else:
        return {"message": "Failed to obtain FDM token"}


#****** NETWORK OBJECTS **************


# Get network objects
@app.get("/network_objects", tags=["NETWORK OBJECTS"])
def get_network(token: str):
    url = "https://10.10.20.65/api/fdm/latest/object/networks"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(url, headers=headers, verify=False)
    return response.json()

# Post network objects
@app.post("/create_network_object", tags=["NETWORK OBJECTS"])
def create_network_object(network_data: dict, token: str):
    url = "https://10.10.20.65/api/fdm/latest/object/networks"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    response = requests.post(url, json=network_data, headers=headers, verify=False)
    return response.json()

# Delete network objects
@app.delete("/delete_network_object/{object_id}", tags=["NETWORK OBJECTS"])
def delete_network_object(object_id: str, token: str):
    url = f"https://10.10.20.65/api/fdm/latest/object/networks/{object_id}"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    response = requests.delete(url, headers=headers, verify=False)
    if response.status_code == 200:
        return {"message": "Network object deleted successfully"}
    else:
        return {"error": "Unable to delete network object"}

# Update network objects
@app.put("/update_network_object/{object_id}", tags=["NETWORK OBJECTS"])
def update_network_object(object_id: str, network_object_data: dict, token: str):
    url = f"https://10.10.20.65/api/fdm/latest/object/networks/{object_id}"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    response = requests.put(url, json=network_object_data, headers=headers, verify=False)
    return response.json()


#********** ACCESS POLICY *********

#Get Access-policy-id
@app.get("/access-policies",  tags=["ACCESS POLICY"])
def get_access_policies(token: str):
    url = "https://10.10.20.65/api/fdm/latest/policy/accesspolicies"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(url, headers=headers, verify=False)
    id = response.json().get("items")
    parent_id = id[0].get('id')
    return parent_id

#Get Access rules
@app.get("/get_access_rules", tags=["ACCESS POLICY"])
def get_access_rules(policy_id: str, token: str):
    url = f"https://10.10.20.65/api/fdm/latest/policy/accesspolicies/{policy_id}/accessrules"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(url, headers=headers, verify=False)
    return response.json()

# Post Access rules
@app.post("/create_access_rule", tags=["ACCESS POLICY"])
def create_access_rule(policy_id: str, access_rule_data: dict, token: str):
    url = f"https://10.10.20.65/api/fdm/latest/policy/accesspolicies/{policy_id}/accessrules"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    response = requests.post(url, json=access_rule_data, headers=headers, verify=False)
    return response.json()

# Delete Access rule
@app.delete("/delete_access_rule/{policy_id}/{object_id}", tags=["ACCESS POLICY"])
def delete_access_rule(policy_id: str, object_id: str, token: str):
    url = f"https://10.10.20.65/api/fdm/latest/policy/accesspolicies/{policy_id}/accessrules/{object_id}"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    response = requests.delete(url, headers=headers, verify=False)
    if response.status_code == 200:
        return {"message": "Access rules deleted successfully"}
    else:
        return {"error": "Unable to delete Access rules"}

# Update Access rules
@app.put("/update_access_rule/{object_id}", tags=["ACCESS POLICY"])
def update_access_rule(parent_id: str, object_id: str, access_rule_data: dict, token: str):
    url = f"https://10.10.20.65/api/fdm/latest/policy/accesspolicies/{parent_id}/accessrules/{object_id}"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    response = requests.put(url, json=access_rule_data, headers=headers, verify=False)
    return response.json()


#********** PORT OBJECTS **********


# Get port objects
@app.get("/get_port_objects", tags=["PORT OBJECTS"])
def get_port_objects(limit: int, token: str):
    url = "https://10.10.20.65/api/fdm/latest/object/tcpports"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    params = {
        "limit": limit
    }
    response = requests.get(url, headers=headers, params=params, verify=False)
    return response.json()


# Post Port Objects
@app.post("/create_port_object", tags=["PORT OBJECTS"])
def create_port_object(port_data: dict, token: str):
    url = "https://10.10.20.65/api/fdm/latest/object/tcpports"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    response = requests.post(url, json=port_data, headers=headers, verify=False)
    return response.json()


# Delete Port objects
@app.delete("/delete_port_object/{port_id}", tags=["PORT OBJECTS"])
def delete_port_object(port_id: str, token: str):
    url = f"https://10.10.20.65/api/fdm/latest/object/ports/{port_id}"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    response = requests.delete(url, headers=headers, verify=False)
    if response.status_code == 200:
        return {"message": "Port objects deleted successfully"}
    else:
        return {"message": "Port object deleted successfully"}


# Update Port objects
@app.put("/update_port_object/{object_id}", tags=["PORT OBJECTS"])
def update_port_object(port_id: str,  port_object_data: dict, token: str):
    url = f"https://10.10.20.65/api/fdm/latest/object/ports/{port_id}"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    response = requests.put(url, json=port_object_data, headers=headers, verify=False)

    return response.json()


#************ NAT RULES ****************

#***********AUTO_NAT_RULES**********

# Get NAT Object ID
def get_nat_objectid():
    url = "https://10.10.20.65/api/fdm/latest/policy/objectnatpolicies"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(url, headers=headers, verify=False)
    object_natid = response.json().get("items")
    parentId = object_natid[0].get('id')
    return parentId


# Get NAT rules
def get_nat_rules(parent_id):
    url = f"https://10.10.20.65/api/fdm/latest/policy/objectnatpolicies/{parent_id}/objectnatrules"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(url, headers=headers, verify=False)
    return response.json()


# Create NAT rule
def create_nat_rule(parent_id, nat_rule_data):
    url = f"https://10.10.20.65/api/fdm/latest/policy/objectnatpolicies/{parent_id}/objectnatrules"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    response = requests.post(url, json=nat_rule_data, headers=headers, verify=False)
    return response.json()


# Delete NAT rule
def delete_nat_rule(parent_id, object_id):
    url = f"https://10.10.20.65/api/fdm/latest/policy/objectnatpolicies/{parent_id}/objectnatrules/{object_id}"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    response = requests.delete(url, headers=headers, verify=False)
    if response.status_code != 200:
        return {"message": "AUTO NAT rules deleted successfully"}
    else:
        return {"message": "AUTO NAT rules deleted successfully"}


# Update NAT rule
def update_nat_rule(parent_id, object_id, nat_rule_data):
    url = f"https://10.10.20.65/api/fdm/latest/policy/objectnatpolicies/{parent_id}/objectnatrules/{object_id}"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    response = requests.put(url, json=nat_rule_data, headers=headers, verify=False)
    return response.json()

# Call the functions with the required parameters
parent_id = get_nat_objectid()
print(get_nat_rules(parent_id))


#*******MANUAL_NAT_RULES**************


# Get MANUAL NAT rules
@app.get("/manual_natid", tags=["MANUAL NAT RULES"])
def get_nat_objectid(token: str):
    url = "https://10.10.20.65/api/fdm/latest/policy/manualnatpolicies"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(url, headers=headers, verify=False)
    return response.json()


@app.get("/manual_nat", tags=["MANUAL NAT RULES"])
def get_nat_rules(parent_id: str, token: str):
    url = f"https://10.10.20.65/api/fdm/latest//policy/manualnatpolicies/{parent_id}/manualnatrules"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(url, headers=headers, verify=False)
    return response.json()


# Post MANUAL NAT rules
@app.post("/create_manual_nat", tags=["MANUAL NAT RULES"])
def create_nat_rule(parent_id: str, nat_rule_data: dict, token: str):
    url = f"https://10.10.20.65/api/fdm/latest/policy/manualnatpolicies/{parent_id}/manualnatrules"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    response = requests.post(url, json=nat_rule_data, headers=headers, verify=False)
    return response.json()


# Delete MANUAL NAT rules
@app.delete("/delete_manual_rule/{policy_id}/{rule_id}", tags=["MANUAL NAT RULES"])
def delete_nat_rule(parent_id: str, object_id: str, token: str):
    url = f"https://10.10.20.65/api/fdm/latest/policy/manualnatpolicies/{parent_id}/manualnatrules/{object_id}"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    response = requests.delete(url, headers=headers, verify=False)
    if response.status_code != 200:
        return {"message": "MANUAL NAT rules deleted successfully"}
    else:
        return {"message": "MANUAL NAT rules deleted successfully"}

# Update MANUAL NAT rules
@app.put("/update_manual_rule/{rule_id}", tags=["MANUAL NAT RULES"])
def update_nat_rule(parent_id: str, object_id: str, nat_rule_data: dict, token: str):
    url = f"https://10.10.20.65/api/fdm/latest/policy/manualnatpolicies/{parent_id}/manualnatrules/{object_id}"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    response = requests.put(url, json=nat_rule_data, headers=headers, verify=False)
    return response.json()


# Run the FastAPI app
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)





