# Cisco-FDM-Integration-Using_FastAPI
FastAPI application provides a set of endpoints to interact with the Cisco Firepower Device Manager (FDM) API.

# FastAPI Integration for FDM

This repository contains a FastAPI application for integrating with the Cisco Firepower Device Management (FDM) system. It provides a RESTful API for managing network objects, access policies, port objects, and NAT rules within the FDM system.

# Table of Contents

  * Getting Started
  * Authentication
  * API Endpoints
  * Usage Examples

# Getting Started

To run this FastAPI application, follow these steps:

   1.Clone the repository to your local machine:

            git clone https://github.com/VijayaVijayanS/FDM-Integration-using_FastAPI.git
            
            cd FDM-Integration-using_FastAPI


   2.Install the required dependencies:

            pip install -r requirements.txt


   3.Update the USERNAME and PASSWORD variables in the main.py file with your FDM credentials.


   4.Run the FastAPI application:

           uvicorn main:app --host 0.0.0.0 --port 8000


   The FastAPI application will start and be accessible at http://localhost:8000.


   # Authentication
   
   This application requires authentication to interact with the FDM system. You need to provide your FDM username and password in the main.py file. You may also need to adjust the FDM 
   API URL if it's different from the default.


  # API Endpoints
  
   The FastAPI application exposes the following API endpoints:

   * GET /get-token: Retrieves an authentication token from the FDM system.

   * Network Objects:
     
        * GET /network_objects: Retrieves network objects.
        * POST /create_network_object: Creates a new network object.
        * DELETE /delete_network_object/{object_id}: Deletes a network object.
        * PUT /update_network_object/{object_id}: Updates a network object.
         
   * Access Policy:
    
        * GET /access-policies: Retrieves the ID of the access policy.
        * GET /get_access_rules: Retrieves access rules for a specific policy.
        * POST /create_access_rule: Creates a new access rule for a specific policy.
        * DELETE /delete_access_rule/{policy_id}/{object_id}: Deletes an access rule.
        * PUT /update_access_rule/{object_id}: Updates an access rule.

   * Port Objects:
  
       * GET /get_port_objects: Retrieves port objects.
       * POST /create_port_object: Creates a new port object.
       * DELETE /delete_port_object/{port_id}: Deletes a port object.
       * PUT /update_port_object/{object_id}: Updates a port object.

   * NAT Rules:
   * Auto NAT Rules:
       
     * GET /get_nat_rules: Retrieves NAT rules for auto NAT policies.
     * POST /create_nat_rule: Creates a new NAT rule for auto NAT policies.
     * DELETE /delete_nat_rule/{object_id}: Deletes a NAT rule for auto NAT policies.
     * PUT /update_nat_rule/{object_id}: Updates a NAT rule for auto NAT policies.
   * Manual NAT Rules:
      
     * GET /manual_natid: Retrieves the ID of the manual NAT policy.
     * GET /manual_nat: Retrieves manual NAT rules for a specific policy.
     * POST /create_manual_nat: Creates a new manual NAT rule for a specific policy.
     * DELETE /delete_manual_rule/{policy_id}/{rule_id}: Deletes a manual NAT rule.
     * PUT /update_manual_rule/{rule_id}: Updates a manual NAT rule.
     

# Usage Examples:

   You can use the provided API endpoints to interact with the FDM system programmatically. Here are some examples:

1.Retrieve an authentication token:

         GET /get-token

2.Create a new network object:

        POST /create_network_object

Request Body:

        {
        "name": "MyNetwork",
        "subnet": "192.168.0.0/24"
        }

3.Retrieve network objects:

        GET /network_objects

4.Update a network object:

        PUT /update_network_object/{object_id}

 Request Body:

      {
      "name": "UpdatedNetwork",
      "subnet": "10.0.0.0/24"
      }

5.Delete a network object:

      DELETE /delete_network_object/{object_id}

** Similar examples for access policies, port objects, and NAT rules.
