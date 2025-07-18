# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-28T18:55:46+00:00



import argparse
import json
import os
from datetime import datetime
from typing import *
from typing import Optional, Union

from autogen.mcp.mcp_proxy import MCPProxy
from autogen.mcp.mcp_proxy.security import BaseSecurity, UnsuportedSecurityStub
from fastapi import Header, Query
from pydantic import conint

from models import (
    Schema1,
    SortOrder,
    Status,
    V1ChargestationsIdPatchResponse,
    V1ChargestationsPostResponse,
    V1CommandsCancelreservationPostRequest,
    V1CommandsCancelreservationPostResponse,
    V1CommandsChargingscheduleDeleteRequest,
    V1CommandsChargingscheduleDeleteResponse,
    V1CommandsChargingschedulePostRequest,
    V1CommandsChargingschedulePostResponse,
    V1CommandsIdVariablesPatchRequest,
    V1CommandsIdVariablesPatchResponse,
    V1CommandsRemotestartPostRequest,
    V1CommandsRemotestartPostResponse,
    V1CommandsRemotestopPostRequest,
    V1CommandsReservePostRequest,
    V1CommandsReservePostResponse,
    V1CommandsResetPostRequest,
    V1CommandsResetPostResponse,
    V1CommandsUnlockconnectorPostRequest,
    V1CommandsUnlockconnectorPostResponse,
    V1ConfigurationsPostRequest,
    V1ConfigurationsPostResponse,
    V1ConnectorsIdPatchRequest,
    V1ConnectorsIdPatchResponse,
    V1ConnectorsPostRequest,
    V1ConnectorsPostResponse,
    V1DriversGetResponse,
    V1DriversIdPatchRequest,
    V1DriversIdPatchResponse,
    V1DriversPostRequest,
    V1DriversPostResponse,
    V1LocationIdPatchRequest,
    V1LocationIdPatchResponse,
    V1LocationsPostRequest,
    V1LocationsPostResponse,
    V1OrganizationsIdPatchRequest,
    V1ReservationsIdPatchRequest,
    V1ReservationsIdPatchResponse,
    V1TokensGetResponse,
    V1TokensIdPatchRequest,
    V1TokensIdPatchResponse,
    V1TokensPostRequest,
    V1TokensPostResponse,
    V1TransactionsGetResponse,
    V1VehiclesGetResponse,
    V1VehiclesIdChargePostRequest,
    V1VehiclesIdChargePostResponse,
)

app = MCPProxy(
    contact={'email': 'hello@edrv.io', 'name': 'eDRV', 'url': 'https://edrv.io'},
    description='edrv.io API Documentation',
    title='eDRV API',
    version='v1',
    servers=[{'url': '//api.edrv.io'}],
)


@app.get(
    '/v1/chargestations',
    description=""" List all Chargestations """,
    tags=['organization_data_management', 'location_handling'],
    security=[
        UnsuportedSecurityStub(name="None"),
    ],
)
def get_charge_stations(
    organization: Optional[str] = None,
    location: Optional[str] = None,
    online: Optional[bool] = None,
    active: Optional[bool] = None,
    public: Optional[bool] = None,
    paginate_limit: Optional[conint(ge=1, le=1000)] = 20,
    paginate_page: Optional[str] = None,
    paginate_enabled: Optional[bool] = True,
    sort_by: Optional[str] = 'createdAt',
    sort_order: Optional[SortOrder] = 'desc',
    created_at__gte_: Optional[datetime] = Query(None, alias='createdAt[$gte]'),
    created_at__lte_: Optional[datetime] = Query(None, alias='createdAt[$lte]'),
    updated_at__gte_: Optional[datetime] = Query(None, alias='updatedAt[$gte]'),
    updated_at__lte_: Optional[datetime] = Query(None, alias='updatedAt[$lte]'),
    include_location: Optional[bool] = None,
    include_evses: Optional[bool] = None,
    include_organization: Optional[bool] = None,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/v1/chargestations',
    description=""" Create a new charge station """,
    tags=['charge_station_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
    ],
)
def post_charge_stations(body: Schema1):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.delete(
    '/v1/chargestations/{id}',
    description=""" Use to delete a charge station """,
    tags=['driver_profile_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
    ],
)
def delete_charge_station(id: str):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1/chargestations/{id}',
    description=""" Get a single charge station's data """,
    tags=['organization_data_management', 'location_handling'],
    security=[
        UnsuportedSecurityStub(name="None"),
    ],
)
def get_charge_station(
    id: str,
    include_location: Optional[bool] = None,
    include_evses: Optional[bool] = None,
    include_organization: Optional[bool] = None,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.patch(
    '/v1/chargestations/{id}',
    description=""" Update a charge station's data """,
    tags=[
        'charge_station_management',
        'charge_station_operations',
        'connector_management',
        'driver_profile_management',
        'settings_configuration',
        'location_handling',
        'organization_data_management',
        'reservation_system_management',
        'token_system_management',
        'financial_transaction_management',
        'vehicle_inventory_management',
    ],
    security=[
        UnsuportedSecurityStub(name="None"),
    ],
)
def patch_charge_station(id: str, body: Schema1 = ...):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1/chargestations/{id}/connectors',
    description=""" List connectors for a chargestation """,
    tags=['charge_station_management', 'organization_data_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
    ],
)
def get_charge_station_connectors(
    id: str,
    include_evse: Optional[bool] = None,
    include_organization: Optional[bool] = None,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1/commands',
    description=""" Get Commands data """,
    tags=[
        'charge_station_management',
        'driver_profile_management',
        'organization_data_management',
        'settings_configuration',
    ],
    security=[
        UnsuportedSecurityStub(name="None"),
    ],
)
def get_commands(
    paginate_limit: Optional[conint(ge=1, le=1000)] = 20,
    paginate_page: Optional[str] = None,
    paginate_enabled: Optional[bool] = True,
    sort_by: Optional[str] = 'createdAt',
    sort_order: Optional[SortOrder] = 'desc',
    created_at__gte_: Optional[datetime] = Query(None, alias='createdAt[$gte]'),
    created_at__lte_: Optional[datetime] = Query(None, alias='createdAt[$lte]'),
    updated_at__gte_: Optional[datetime] = Query(None, alias='updatedAt[$gte]'),
    updated_at__lte_: Optional[datetime] = Query(None, alias='updatedAt[$lte]'),
    include_chargestation: Optional[bool] = None,
    include_driver: Optional[bool] = None,
    include_transaction: Optional[bool] = None,
    include_organization: Optional[bool] = None,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/v1/commands/cancelreservation',
    description=""" Use to request a delete an existing reservation. The request will wait for the charge station to process the command. It will timeout after 60 seconds. """,
    tags=['reservation_system_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
    ],
)
def cancelreservation(body: V1CommandsCancelreservationPostRequest):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.delete(
    '/v1/commands/chargingschedule',
    description=""" Delete a smart charging schedule """,
    tags=['charge_station_operations'],
    security=[
        UnsuportedSecurityStub(name="None"),
    ],
)
def deletechargingschedule(body: V1CommandsChargingscheduleDeleteRequest):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/v1/commands/chargingschedule',
    description=""" Set one of charging power or current of a specific chargestation connector """,
    tags=['charge_station_operations'],
    security=[
        UnsuportedSecurityStub(name="None"),
    ],
)
def setchargingschedule(body: V1CommandsChargingschedulePostRequest):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/v1/commands/remotestart',
    description=""" Use to request a remote start command. The request will wait for the charge station to process the command. It will timeout after 60 seconds. """,
    tags=['charge_station_operations'],
    security=[
        UnsuportedSecurityStub(name="None"),
    ],
)
def remotestart(body: V1CommandsRemotestartPostRequest):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/v1/commands/remotestop',
    description=""" Use to request a remote stop command. The request will wait for the charge station to process the command. It will timeout after 60 seconds. """,
    tags=['charge_station_operations'],
    security=[
        UnsuportedSecurityStub(name="None"),
    ],
)
def remotestop(body: V1CommandsRemotestopPostRequest):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/v1/commands/reserve',
    description=""" Use to request a reserve command. The request will wait for the charge station to process the command. It will timeout after 60 seconds. """,
    tags=['charge_station_operations', 'reservation_system_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
    ],
)
def reserve(body: V1CommandsReservePostRequest):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/v1/commands/reset',
    description=""" Use to request a reset command. The request will wait for the charge station to process the command. It will timeout after 60 seconds. """,
    tags=['charge_station_operations'],
    security=[
        UnsuportedSecurityStub(name="None"),
    ],
)
def reset(body: V1CommandsResetPostRequest):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/v1/commands/unlockconnector',
    description=""" Use to request an unlock command for a connector. The request will wait for the charge station to process the command. It will timeout after 60 seconds. """,
    tags=['connector_management', 'charge_station_operations'],
    security=[
        UnsuportedSecurityStub(name="None"),
    ],
)
def unlockconnector(body: V1CommandsUnlockconnectorPostRequest):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1/commands/{id}/variables',
    description=""" Get a charge station's config variables """,
    tags=[
        'charge_station_management',
        'charge_station_operations',
        'connector_management',
        'driver_profile_management',
        'settings_configuration',
        'location_handling',
        'organization_data_management',
        'reservation_system_management',
        'token_system_management',
        'financial_transaction_management',
        'vehicle_inventory_management',
    ],
    security=[
        UnsuportedSecurityStub(name="None"),
    ],
)
def get_variables(id: str):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.patch(
    '/v1/commands/{id}/variables',
    description=""" Update config variables for a chargestation """,
    tags=['charge_station_operations'],
    security=[
        UnsuportedSecurityStub(name="None"),
    ],
)
def patch_charge_station_variable(
    id: str, body: V1CommandsIdVariablesPatchRequest = ...
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1/configurations',
    description=""" Get Configurations data """,
    tags=['settings_configuration'],
    security=[
        UnsuportedSecurityStub(name="None"),
    ],
)
def get_configurations(
    paginate_limit: Optional[conint(ge=1, le=1000)] = 20,
    paginate_page: Optional[str] = None,
    paginate_enabled: Optional[bool] = True,
    sort_by: Optional[str] = 'createdAt',
    sort_order: Optional[SortOrder] = 'desc',
    created_at__gte_: Optional[datetime] = Query(None, alias='createdAt[$gte]'),
    created_at__lte_: Optional[datetime] = Query(None, alias='createdAt[$lte]'),
    updated_at__gte_: Optional[datetime] = Query(None, alias='updatedAt[$gte]'),
    updated_at__lte_: Optional[datetime] = Query(None, alias='updatedAt[$lte]'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/v1/configurations',
    description=""" Create connector with parameters """,
    tags=['settings_configuration'],
    security=[
        UnsuportedSecurityStub(name="None"),
    ],
)
def post_configurations(body: V1ConfigurationsPostRequest):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1/configurations/{id}',
    description=""" Get one Configuration data """,
    tags=[
        'charge_station_management',
        'charge_station_operations',
        'connector_management',
        'driver_profile_management',
        'settings_configuration',
        'location_handling',
        'organization_data_management',
        'reservation_system_management',
        'token_system_management',
        'financial_transaction_management',
        'vehicle_inventory_management',
    ],
    security=[
        UnsuportedSecurityStub(name="None"),
    ],
)
def get_configuration(id: str):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1/connectors',
    description=""" List connectors """,
    tags=[
        'charge_station_management',
        'charge_station_operations',
        'settings_configuration',
        'location_handling',
        'organization_data_management',
    ],
    security=[
        UnsuportedSecurityStub(name="None"),
    ],
)
def get_connectors(
    paginate_limit: Optional[conint(ge=1, le=1000)] = 20,
    paginate_page: Optional[str] = None,
    paginate_enabled: Optional[bool] = True,
    sort_by: Optional[str] = 'createdAt',
    sort_order: Optional[SortOrder] = 'desc',
    created_at__gte_: Optional[datetime] = Query(None, alias='createdAt[$gte]'),
    created_at__lte_: Optional[datetime] = Query(None, alias='createdAt[$lte]'),
    updated_at__gte_: Optional[datetime] = Query(None, alias='updatedAt[$gte]'),
    updated_at__lte_: Optional[datetime] = Query(None, alias='updatedAt[$lte]'),
    include_evse: Optional[bool] = None,
    include_organization: Optional[bool] = None,
    include_rate: Optional[bool] = None,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/v1/connectors',
    description=""" Create a new connector """,
    tags=['connector_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
    ],
)
def post_connectors(body: V1ConnectorsPostRequest):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.delete(
    '/v1/connectors/{id}',
    description=""" Delete a connector """,
    tags=['charge_station_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
    ],
)
def delete_connector(id: str):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1/connectors/{id}',
    description=""" Get a connector """,
    tags=['charge_station_management', 'organization_data_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
    ],
)
def get_connector(
    id: str,
    include_evse: Optional[bool] = None,
    include_organization: Optional[bool] = None,
    include_rate: Optional[bool] = None,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.patch(
    '/v1/connectors/{id}',
    description=""" Update a connector's data """,
    tags=['connector_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
    ],
)
def patch_connector(id: str, body: V1ConnectorsIdPatchRequest = ...):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1/drivers',
    description=""" List all drivers """,
    tags=['settings_configuration', 'organization_data_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
    ],
)
def get_drivers(
    active: Optional[bool] = None,
    paginate_limit: Optional[conint(ge=1, le=1000)] = 20,
    paginate_page: Optional[str] = None,
    paginate_enabled: Optional[bool] = True,
    sort_by: Optional[str] = 'createdAt',
    sort_order: Optional[SortOrder] = 'desc',
    created_at__gte_: Optional[datetime] = Query(None, alias='createdAt[$gte]'),
    created_at__lte_: Optional[datetime] = Query(None, alias='createdAt[$lte]'),
    updated_at__gte_: Optional[datetime] = Query(None, alias='updatedAt[$gte]'),
    updated_at__lte_: Optional[datetime] = Query(None, alias='updatedAt[$lte]'),
    include_tokens: Optional[bool] = None,
    include_group: Optional[bool] = None,
    include_organization: Optional[bool] = None,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/v1/drivers',
    description=""" Create a new driver """,
    tags=['driver_profile_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
    ],
)
def post_drivers(body: V1DriversPostRequest):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.delete(
    '/v1/drivers/{id}',
    description=""" Delete a driver """,
    tags=['driver_profile_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
    ],
)
def delete_driver(id: str):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1/drivers/{id}',
    description=""" Get a driver's data """,
    tags=['organization_data_management', 'token_system_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
    ],
)
def get_driver(
    id: str,
    include_tokens: Optional[bool] = None,
    include_group: Optional[bool] = None,
    include_organization: Optional[bool] = None,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.patch(
    '/v1/drivers/{id}',
    description=""" Update a driver's data """,
    tags=['driver_profile_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
    ],
)
def patch_driver(id: str, body: V1DriversIdPatchRequest = ...):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.delete(
    '/v1/location/{id}',
    description=""" Delete a location """,
    tags=['charge_station_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
    ],
)
def delete_location(id: str):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1/location/{id}',
    description=""" Get a location's data """,
    tags=['organization_data_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
    ],
)
def get_location(
    id: str,
    include_chargestations: Optional[bool] = None,
    include_organization: Optional[bool] = None,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.patch(
    '/v1/location/{id}',
    description=""" Update a location's data """,
    tags=['location_handling'],
    security=[
        UnsuportedSecurityStub(name="None"),
    ],
)
def patch_location(id: str, body: V1LocationIdPatchRequest = ...):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1/locations',
    description=""" Get Locations data """,
    tags=['organization_data_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
    ],
)
def get_locations(
    paginate_limit: Optional[conint(ge=1, le=1000)] = 20,
    paginate_page: Optional[str] = None,
    paginate_enabled: Optional[bool] = True,
    sort_by: Optional[str] = 'createdAt',
    sort_order: Optional[SortOrder] = 'desc',
    created_at__gte_: Optional[datetime] = Query(None, alias='createdAt[$gte]'),
    created_at__lte_: Optional[datetime] = Query(None, alias='createdAt[$lte]'),
    updated_at__gte_: Optional[datetime] = Query(None, alias='updatedAt[$gte]'),
    updated_at__lte_: Optional[datetime] = Query(None, alias='updatedAt[$lte]'),
    include_organization: Optional[bool] = None,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/v1/locations',
    description=""" Create a new location """,
    tags=['location_handling'],
    security=[
        UnsuportedSecurityStub(name="None"),
    ],
)
def post_locations(body: V1LocationsPostRequest):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1/organizations',
    description=""" Get an array of all Organizations """,
    tags=[
        'settings_configuration',
        'location_handling',
        'organization_data_management',
    ],
    security=[
        UnsuportedSecurityStub(name="None"),
    ],
)
def get_organizations(
    paginate_limit: Optional[conint(ge=1, le=1000)] = 20,
    paginate_page: Optional[str] = None,
    paginate_enabled: Optional[bool] = True,
    sort_by: Optional[str] = 'createdAt',
    sort_order: Optional[SortOrder] = 'desc',
    created_at__gte_: Optional[datetime] = Query(None, alias='createdAt[$gte]'),
    created_at__lte_: Optional[datetime] = Query(None, alias='createdAt[$lte]'),
    updated_at__gte_: Optional[datetime] = Query(None, alias='updatedAt[$gte]'),
    updated_at__lte_: Optional[datetime] = Query(None, alias='updatedAt[$lte]'),
    include_locations: Optional[bool] = None,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1/organizations/{id}',
    description=""" Get one organization's data by id """,
    tags=['location_handling'],
    security=[
        UnsuportedSecurityStub(name="None"),
    ],
)
def get_organization(id: str, include_locations: Optional[bool] = None):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.patch(
    '/v1/organizations/{id}',
    description=""" Update an organization's data """,
    tags=['organization_data_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
    ],
)
def patch_organization(id: str, body: V1OrganizationsIdPatchRequest = ...):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1/realtime',
    description=""" Use to request a Websockets handshake """,
    tags=['settings_configuration'],
    security=[
        UnsuportedSecurityStub(name="None"),
    ],
)
def get_realtime(
    sec_websocket_protocol: str = Header(..., alias='sec-websocket-protocol')
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1/reservations',
    description=""" Get Reservations data """,
    tags=[
        'charge_station_management',
        'settings_configuration',
        'organization_data_management',
    ],
    security=[
        UnsuportedSecurityStub(name="None"),
    ],
)
def get_reservations(
    paginate_limit: Optional[conint(ge=1, le=1000)] = 20,
    paginate_page: Optional[str] = None,
    paginate_enabled: Optional[bool] = True,
    sort_by: Optional[str] = 'createdAt',
    sort_order: Optional[SortOrder] = 'desc',
    created_at__gte_: Optional[datetime] = Query(None, alias='createdAt[$gte]'),
    created_at__lte_: Optional[datetime] = Query(None, alias='createdAt[$lte]'),
    updated_at__gte_: Optional[datetime] = Query(None, alias='updatedAt[$gte]'),
    updated_at__lte_: Optional[datetime] = Query(None, alias='updatedAt[$lte]'),
    include_chargestation: Optional[bool] = None,
    include_organization: Optional[bool] = None,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1/reservations/{id}',
    description=""" Get one reservation data """,
    tags=['organization_data_management', 'settings_configuration'],
    security=[
        UnsuportedSecurityStub(name="None"),
    ],
)
def get_reservation(
    id: str,
    include_chargestation: Optional[bool] = None,
    include_organization: Optional[bool] = None,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.patch(
    '/v1/reservations/{id}',
    description=""" Use to request a update an existing reservation. The request will wait for the charge station to process the command. It will timeout after 60 seconds. """,
    tags=['reservation_system_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
    ],
)
def updatereservation(id: str, body: V1ReservationsIdPatchRequest = ...):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1/tokens',
    description=""" List tokens """,
    tags=['charge_station_management', 'settings_configuration'],
    security=[
        UnsuportedSecurityStub(name="None"),
    ],
)
def get_tokens(
    paginate_limit: Optional[conint(ge=1, le=1000)] = 20,
    paginate_page: Optional[str] = None,
    paginate_enabled: Optional[bool] = True,
    sort_by: Optional[str] = 'createdAt',
    sort_order: Optional[SortOrder] = 'desc',
    created_at__gte_: Optional[datetime] = Query(None, alias='createdAt[$gte]'),
    created_at__lte_: Optional[datetime] = Query(None, alias='createdAt[$lte]'),
    updated_at__gte_: Optional[datetime] = Query(None, alias='updatedAt[$gte]'),
    updated_at__lte_: Optional[datetime] = Query(None, alias='updatedAt[$lte]'),
    include_driver: Optional[bool] = None,
    include_organization: Optional[bool] = None,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/v1/tokens',
    description=""" Create a new token """,
    tags=['token_system_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
    ],
)
def post_tokens(body: V1TokensPostRequest):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.delete(
    '/v1/tokens/{id}',
    description=""" Use to delete a token """,
    tags=['charge_station_operations'],
    security=[
        UnsuportedSecurityStub(name="None"),
    ],
)
def delete_token(id: str):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1/tokens/{id}',
    description=""" Get a single token's data """,
    tags=['driver_profile_management', 'organization_data_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
    ],
)
def get_token(
    id: str,
    include_driver: Optional[bool] = None,
    include_organization: Optional[bool] = None,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.patch(
    '/v1/tokens/{id}',
    description=""" Update a token """,
    tags=['token_system_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
    ],
)
def patch_token(id: str, body: V1TokensIdPatchRequest = ...):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1/transactions',
    description=""" Get a list of transactions """,
    tags=[
        'charge_station_management',
        'settings_configuration',
        'organization_data_management',
    ],
    security=[
        UnsuportedSecurityStub(name="None"),
    ],
)
def get_transactions(
    status: Optional[Status] = None,
    paginate_limit: Optional[conint(ge=1, le=1000)] = 20,
    paginate_page: Optional[str] = None,
    paginate_enabled: Optional[bool] = True,
    sort_by: Optional[str] = 'createdAt',
    sort_order: Optional[SortOrder] = 'desc',
    created_at__gte_: Optional[datetime] = Query(None, alias='createdAt[$gte]'),
    created_at__lte_: Optional[datetime] = Query(None, alias='createdAt[$lte]'),
    updated_at__gte_: Optional[datetime] = Query(None, alias='updatedAt[$gte]'),
    updated_at__lte_: Optional[datetime] = Query(None, alias='updatedAt[$lte]'),
    include_chargestation: Optional[bool] = None,
    include_evse: Optional[bool] = None,
    include_connector: Optional[bool] = None,
    include_driver: Optional[bool] = None,
    include_token: Optional[bool] = None,
    include_reservation: Optional[bool] = None,
    include_organization: Optional[bool] = None,
    include_rate: Optional[bool] = None,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1/transactions/{id}',
    description=""" Get a specific transaction """,
    tags=[
        'charge_station_management',
        'charge_station_operations',
        'connector_management',
        'driver_profile_management',
        'settings_configuration',
        'organization_data_management',
        'reservation_system_management',
        'token_system_management',
    ],
    security=[
        UnsuportedSecurityStub(name="None"),
    ],
)
def get_transaction(
    id: str,
    include_chargestation: Optional[bool] = None,
    include_evse: Optional[bool] = None,
    include_connector: Optional[bool] = None,
    include_driver: Optional[bool] = None,
    include_token: Optional[bool] = None,
    include_reservation: Optional[bool] = None,
    include_organization: Optional[bool] = None,
    include_rate: Optional[bool] = None,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1/transactions/{id}/cost',
    description=""" Get a specific transaction's cost """,
    tags=[
        'charge_station_management',
        'charge_station_operations',
        'connector_management',
        'driver_profile_management',
        'settings_configuration',
        'location_handling',
        'organization_data_management',
        'reservation_system_management',
        'token_system_management',
        'financial_transaction_management',
        'vehicle_inventory_management',
    ],
    security=[
        UnsuportedSecurityStub(name="None"),
    ],
)
def get_transaction_cost(id: str):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1/vehicles',
    description=""" List all vehicles """,
    tags=[
        'charge_station_management',
        'charge_station_operations',
        'settings_configuration',
    ],
    security=[
        UnsuportedSecurityStub(name="None"),
    ],
)
def get_vehicles(
    active: Optional[bool] = None,
    paginate_limit: Optional[conint(ge=1, le=1000)] = 20,
    paginate_page: Optional[str] = None,
    paginate_enabled: Optional[bool] = True,
    sort_by: Optional[str] = 'createdAt',
    sort_order: Optional[SortOrder] = 'desc',
    created_at__gte_: Optional[datetime] = Query(None, alias='createdAt[$gte]'),
    created_at__lte_: Optional[datetime] = Query(None, alias='createdAt[$lte]'),
    updated_at__gte_: Optional[datetime] = Query(None, alias='updatedAt[$gte]'),
    updated_at__lte_: Optional[datetime] = Query(None, alias='updatedAt[$lte]'),
    include_driver: Optional[bool] = None,
    include_token: Optional[bool] = None,
    include_organization: Optional[bool] = None,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1/vehicles/{id}',
    description=""" Get a vehicle's data """,
    tags=[
        'driver_profile_management',
        'token_system_management',
        'organization_data_management',
    ],
    security=[
        UnsuportedSecurityStub(name="None"),
    ],
)
def get_vehicle(
    id: str,
    include_driver: Optional[bool] = None,
    include_token: Optional[bool] = None,
    include_organization: Optional[bool] = None,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1/vehicles/{id}/battery',
    description=""" Get a vehicle's battery """,
    tags=[
        'charge_station_management',
        'charge_station_operations',
        'connector_management',
        'driver_profile_management',
        'settings_configuration',
        'location_handling',
        'organization_data_management',
        'reservation_system_management',
        'token_system_management',
        'financial_transaction_management',
        'vehicle_inventory_management',
    ],
    security=[
        UnsuportedSecurityStub(name="None"),
    ],
)
def get_vehicle_battery(id: str):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1/vehicles/{id}/charge',
    description=""" Get a vehicle's charge """,
    tags=[
        'charge_station_management',
        'charge_station_operations',
        'connector_management',
        'driver_profile_management',
        'settings_configuration',
        'location_handling',
        'organization_data_management',
        'reservation_system_management',
        'token_system_management',
        'financial_transaction_management',
        'vehicle_inventory_management',
    ],
    security=[
        UnsuportedSecurityStub(name="None"),
    ],
)
def get_vehicle_charge(id: str):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/v1/vehicles/{id}/charge',
    description=""" Change charge """,
    tags=['charge_station_operations'],
    security=[
        UnsuportedSecurityStub(name="None"),
    ],
)
def post_charge(id: str, body: V1VehiclesIdChargePostRequest = ...):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1/vehicles/{id}/location',
    description=""" Get a vehicle's location """,
    tags=['driver_profile_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
    ],
)
def get_vehicle_location(id: str):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1/vehicles/{id}/odometer',
    description=""" Get a vehicle's odometer """,
    tags=['driver_profile_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
    ],
)
def get_vehicle_odometer(id: str):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MCP Server")
    parser.add_argument(
        "transport",
        choices=["stdio", "sse", "streamable-http"],
        help="Transport mode (stdio, sse or streamable-http)",
    )
    args = parser.parse_args()

    if "CONFIG_PATH" in os.environ:
        config_path = os.environ["CONFIG_PATH"]
        app.load_configuration(config_path)

    if "CONFIG" in os.environ:
        config = os.environ["CONFIG"]
        app.load_configuration_from_string(config)

    if "SECURITY" in os.environ:
        security_params = BaseSecurity.parse_security_parameters_from_env(
            os.environ,
        )

        app.set_security_params(security_params)

    mcp_settings = json.loads(os.environ.get("MCP_SETTINGS", "{}"))

    app.get_mcp(**mcp_settings).run(transport=args.transport)
