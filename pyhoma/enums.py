import logging
from enum import Enum, IntEnum, unique

_LOGGER = logging.getLogger(__name__)


@unique
class ProductType(IntEnum):
    NONE = 0
    ACTUATOR = 1
    SENSOR = 2
    VIDEO = 3
    CONTROLLABLE = 4
    GATEWAY = 5
    INFRASTRUCTURE_COMPONENT = 6


@unique
class GatewayType(IntEnum):
    UNKNOWN = -1
    VIRTUAL_KIZBOX = 0
    KIZBOX_V1 = 2
    TAHOMA = 15
    VERISURE_ALARM_SYSTEM = 20
    KIZBOX_MINI = 21
    HI_KUMO_ADAPTER = 22  # Hi Kumo Adapter SPX-WFG01 (constant added manually)
    KIZBOX_V2 = 24
    MYFOX_ALARM_SYSTEM = 25
    KIZBOX_MINI_VMBUS = 27
    KIZBOX_MINI_IO = 28
    TAHOMA_V2 = 29
    KIZBOX_V2_3H = 30
    KIZBOX_V2_2H = 31
    COZYTOUCH = 32
    CONNEXOON = 34
    JSW_CAMERA = 35
    TAHOMA_V2_RTS = 41
    KIZBOX_MINI_MODBUS = 42
    KIZBOX_MINI_OVP = 43
    HI_BOX = 44  # Hi Kumo AHP-SMB01 Hi Box (constant added manually)
    CONNEXOON_RTS = 53
    OPENDOORS_LOCK_SYSTEM = 54
    CONNEXOON_RTS_JAPAN = 56
    HOME_PROTECT_SYSTEM = 58
    CONNEXOON_RTS_AUSTRALIA = 62
    THERMOSTAT_SOMFY_SYSTEM = 63
    SMARTLY_MINI_DAUGHTERBOARD_ZWAVE = 65
    SMARTLY_MINIBOX_RAILDIN = 66
    TAHOMA_BEE = 67
    TAHOMA_RAIL_DIN = 72
    NEXITY_RAIL_DIN = 74
    ELIOT = 77
    WISER = 88
    TAHOMA_SWITCH = 98

    @classmethod
    def _missing_(cls, value):  # type: ignore
        _LOGGER.warning(f"Unsupported value {value} has been returned for {cls}")
        return cls.UNKNOWN

    @property
    def beautify_name(self) -> str:
        return self.name.replace("_", " ").title()


@unique
class GatewaySubType(IntEnum):
    UNKNOWN = -1
    TAHOMA_BASIC = 1
    TAHOMA_BASIC_PLUS = 2
    TAHOMA_PREMIUM = 3
    SOMFY_BOX = 4
    HITACHI_BOX = 5
    MONDIAL_BOX = 6
    MAROC_TELECOM_BOX = 7
    TAHOMA_SERENITY = 8
    TAHOMA_VERISURE = 9
    TAHOMA_SERENITY_PREMIUM = 10
    TAHOMA_MONSIEUR_STORE = 11
    TAHOMA_MAISON_AVENIR_ET_TRADITION = 12
    TAHOMA_SHORT_CHANNEL = 13
    TAHOMA_PRO = 14
    TAHOMA_SECURITY_SHORT_CHANNEL = 15
    TAHOMA_SECURITY_PRO = 16
    # TAHOMA_BOX_C_IO = 12 That’s probably 17, but tahomalink.com says it’s 12

    @classmethod
    def _missing_(cls, value):  # type: ignore
        _LOGGER.warning(f"Unsupported value {value} has been returned for {cls}")
        return cls.UNKNOWN

    @property
    def beautify_name(self) -> str:
        return self.name.replace("_", " ").title()


@unique
class DataType(IntEnum):
    NONE = 0
    INTEGER = 1
    FLOAT = 2
    STRING = 3
    BLOB = 4
    DATE = 5
    BOOLEAN = 6
    PASSWORD = 9
    JSON_ARRAY = 10
    JSON_OBJECT = 11


@unique
class ExecutionType(str, Enum):
    IMMEDIATE_EXECUTION = "Immediate execution"
    DELAYED_EXECUTION = "Delayed execution"
    TECHNICAL_EXECUTION = "Technical execution"
    PLANNING = "Planning"
    RAW_TRIGGER_SERVER = "Raw trigger (Server)"
    RAW_TRIGGER_GATEWAY = "Raw trigger (Gateway)"


@unique
class ExecutionState(str, Enum):
    INITIALIZED = "INITIALIZED"
    NOT_TRANSMITTED = "NOT_TRANSMITTED"
    TRANSMITTED = "TRANSMITTED"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    QUEUED_GATEWAY_SIDE = "QUEUED_GATEWAY_SIDE"
    QUEUED_SERVER_SIDE = "QUEUED_SERVER_SIDE"


@unique
class ExecutionSubType(str, Enum):
    ACTION_GROUP = "ACTION_GROUP"
    ACTION_GROUP_SEQUENCE = "ACTION_GROUP_SEQUENCE"
    DAWN_TRIGGER = "DAWN_TRIGGER"
    DUSK_TRIGGER = "DUSK_TRIGGER"
    DISCRETE_TRIGGER_USER = "DISCRETE_TRIGGER_USER"
    GENERIC_COMMAND_SCHEDULING = "GENERIC_COMMAND_SCHEDULING"
    IFT_CONDITION = "IFT_CONDITION"
    INTERNAL = "INTERNAL"
    MANUAL_CONTROL = "MANUAL_CONTROL"
    NO_ERROR = "NO_ERROR"
    P2P_COMMAND_REGULATION = "P2P_COMMAND_REGULATION"
    TIME_TRIGGER = "TIME_TRIGGER"


@unique
class FailureType(IntEnum):
    UNKNOWN = -1
    NO_FAILURE = 0
    NON_EXECUTING = 11
    ERROR_WHILE_EXECUTING = 12
    ACTUATORUNKNOWN = 101
    ACTUATORNOANSWER = 102
    ERRORREADWRITEACCESS = 103
    ERRORCOMMAND = 104
    CMDUNKNOWN = 105
    CMDCANCELLED = 106
    NOREMOTECONTROL = 107
    ERROR_TRANSFER_KEY = 108
    ERRORDATABASE = 109
    MODELOCALENABLED = 110
    BAD_CMD = 111
    BAD_HD = 112
    BAD_LEN = 113
    BAD_ADDRESS = 114
    BAD_PARAM = 115
    NOT_FOUND_ETX = 116
    BAD_CRC_SERIAL = 117
    BAD_STATUS = 118
    KEY_NOT_RECEIVE = 119
    INSERTION_ERROR = 120
    NODE_NOT_VERIFY_WITH_NEW_KEY = 121
    POOL_FULL = 122
    ADDRESS_UNKNOWN = 123
    NODE_CANT_PAIRED = 124
    NODE_CANT_UPDATE_TRANSFER_STATUS = 125
    UNKNOWN_ERROR = 126
    INVALID_CHANNEL = 127
    INVALID_COMMAND = 128
    SERIAL_IO_ERROR = 129
    OPERATION_NOT_ALLOWED = 130
    RESTART_STACK = 131
    INCOMPLETE_DISCOVER = 132
    TRANFER_KEY_NO_REMOTE_CONTROLLER = 133
    TRANFER_KEY_MULTI_REMOTE_CONTROLLER = 134
    RF_PROTOCOL_FATAL_ERROR = 135
    INTERNAL_ERROR = 136
    BUSY_RADIO_ERROR = 137
    BAD_MAC_ERROR = 138
    SETUP_REQUIRED = 139
    MASTER_AUTHENTICATION_FAILED_ERROR = 140
    END_OF_RECEIVING_CONFIGURATION_MODE = 141
    DATA_TRANSPORT_SERVICE_ERROR = 142
    DATA_TRANSPORT_SERVICE_ABORTED_BY_RECIPIENT = 143
    STOPPED_BY_CONFIGURATION_OPERATION_ERROR = 144
    COMMAND_NAME_TYPE_INVALID = 145
    COMMAND_NAME_NOT_INSTALLED_OR_INVALID = 146
    COMMAND_INVALID_LEN_ON_FRAME = 147
    COMMAND_ZONE_INVALID_OR_NOT_INSTALLED = 148
    COMMAND_SENSOR_VALUE_INVALID = 149
    COMMAND_ZONE_TEMPERATURE_INVALID = 150
    COMMAND_DHW_NOT_INSTALLED_OR_INVALID = 151
    COMMAND_INSERTION_FAILED_ERROR = 152
    NONEXEC_BLOCKED_BY_HAZARD = 153
    NONEXEC_OVERHEATING_PROTECTION = 154
    NONEXEC_DEVICE_LIMITATION = 155
    NONEXEC_DOOR_IS_OPENED = 156
    NONEXEC_MAINTENANCE_REQUIRED = 157
    DEAD_SENSOR = 158
    SENSOR_MAINTENANCE_REQUIRED = 159
    NONEXEC_OTHER = 160
    WHILEEXEC_BLOCKED_BY_HAZARD = 161
    WHILEEXEC_OVERHEATING_PROTECTION = 162
    WHILEEXEC_DEVICE_LIMITATION = 163
    WHILEEXEC_DOOR_IS_OPENED = 164
    WHILEEXEC_MAINTENANCE_REQUIRED = 165
    WHILEEXEC_OTHER = 166
    PRIORITY_LOCK__LOCAL_USER = 167
    PRIORITY_LOCK__USER = 168
    PRIORITY_LOCK__RAIN = 169
    PRIORITY_LOCK__TIMER = 170
    PRIORITY_LOCK__SECURITY = 171
    PRIORITY_LOCK__UPS = 172
    PRIORITY_LOCK__SFC = 173
    PRIORITY_LOCK__LSC = 174
    PRIORITY_LOCK__SAAC = 175
    PRIORITY_LOCK__WIND = 176
    PRIORITY_LOCK__EXTERNAL_ACCESS = 177
    PRIORITY_LOCK__EMERGENCY = 178
    NO_DISTANT_FOR_DISCOVER = 179
    ANOTHER_COMMAND_IS_RUNNING = 180
    PROBLEM_WITH_BOILER_COMMUNICATION = 181
    LOCKED_BY_RCM = 182
    RCM_NO_REMOTE_CONTROL = 183
    DISCOVER_NO_REMOTE_CONTROLLER_ERROR = 184
    COMMAND_INTERRUPTED = 185
    PRIORITY_LOCK__WIND_FORCING_AVAILABLE = 190
    PRIORITY_LOCK__WIND_FORCING_UNAVAILABLE = 191
    PRIORITY_LOCK__NO_SECURITY_DEVICE = 192
    PRIORITY_LOCK__DEAD_SENSOR = 193
    PRIORITY_LOCK__UNKNOWN_ERROR = 194
    DBUS_ERROR = 200
    DBUS_NO_MEMORY = 201
    DBUS_SERVICE_UNKNOWN = 202
    DBUS_NAME_HAS_NO_OWNER = 203
    DBUS_NO_REPLY = 204
    DBUS_IO_ERROR = 205
    DBUS_BAD_ADDRESS = 206
    DBUS_NOT_SUPPORTED = 207
    DBUS_LIMITS_EXCEEDED = 208
    DBUS_ACCESS_DENIED = 209
    DBUS_AUTH_FAILED = 210
    DBUS_NO_SERVER = 211
    DBUS_TIMEOUT = 212
    DBUS_NO_NETWORK = 213
    DBUS_ADDRESS_IN_USE = 214
    DBUS_DISCONNECTED = 215
    DBUS_INVALID_ARGS = 216
    DBUS_FILE_NOT_FOUND = 217
    DBUS_FILE_EXISTS = 218
    DBUS_UNKNOWN_METHOD = 219
    DBUS_UNKNOWN_OBJECT = 220
    DBUS_UNKNOWN_INTERFACE = 221
    DBUS_UNKNOWN_PROPERTY = 222
    DBUS_PROPERTY_READ_ONLY = 223
    DBUS_TIMED_OUT = 224
    DBUS_MATCH_RULE_NOT_FOUND = 225
    DBUS_MATCH_RULE_INVALID = 226
    DBUS_SPAWN_EXEC_FAILED = 227
    DBUS_SPAWN_FORK_FAILED = 228
    DBUS_SPAWN_CHILD_EXITED = 229
    DBUS_SPAWN_CHILD_SIGNALED = 230
    DBUS_SPAWN_FAILED = 231
    DBUS_SPAWN_SETUP_FAILED = 232
    DBUS_SPAWN_CONFIG_INVALID = 233
    DBUS_SPAWN_SERVICE_INVALID = 234
    DBUS_SPAWN_SERVICE_NOT_FOUND = 235
    DBUS_SPAWN_PERMISSIONS_INVALID = 236
    DBUS_SPAWN_FILE_INVALID = 237
    DBUS_SPAWN_NO_MEMORY = 238
    DBUS_UNIX_PROCESS_ID_UNKNOWN = 239
    DBUS_INVALID_SIGNATURE = 240
    DBUS_INVALID_FILE_CONTENT = 241
    DBUS_SELINUX_SECURITY_CONTEXT_UNKNOWN = 242
    DBUS_ADT_AUDIT_DATA_UNKNOWN = 243
    DBUS_OBJECT_PATH_IN_USE = 244
    DBUS_INCONSISTENT_MESSAGE = 245
    NOT_IMPLEMENTED_YET = 300
    MODULE_NOT_LOADED = 301
    APPLICATION_NOT_RUNNING = 302
    NONEXEC_MANUALLY_CONTROLLED = 400
    NONEXEC_AUTOMATIC_CYCLE = 401
    NONEXEC_BATTERY_LEVEL = 402
    NONEXEC_WRONG_LOAD_CONNECTED = 403
    NONEXEC_HIGH_CONSUMPTION = 404
    NONEXEC_LOW_CONSUMPTION = 405
    NONEXEC_COLOUR_NOT_REACHABLE = 406
    NONEXEC_USER_ACTION_NEEDED = 407
    NONEXEC_COMMAND_INCOMPATIBLE_WITH_MOVEMENT = 408
    NONEXEC_CANNOT_CHANGE_STATE = 409
    NONEXEC_FILTER_MAINTENANCE = 410
    NONEXEC_OPERATING_MODE_NOT_SUPPORTED = 411
    WHILEEXEC_MANUALLY_CONTROLLED = 420
    WHILEEXEC_AUTOMATIC_CYCLE = 421
    WHILEEXEC_BATTERY_LEVEL = 422
    WHILEEXEC_WRONG_LOAD_CONNECTED = 423
    WHILEEXEC_HIGH_CONSUMPTION = 424
    WHILEEXEC_LOW_CONSUMPTION = 425
    WHILEEXEC_COLOUR_NOT_REACHABLE = 426
    WHILEEXEC_USER_ACTION_NEEDED = 427
    WHILEEXEC_COMMAND_INCOMPATIBLE_WITH_MOVEMENT = 428
    WHILEEXEC_CANNOT_CHANGE_STATE = 429
    WHILEEXEC_FILTER_MAINTENANCE = 430
    WHILEEXEC_OPERATING_MODE_NOT_SUPPORTED = 431
    OVERRIDEMODE_ERROR = 450
    CAMERA_INVALID_CREDENTIALS = 500
    UNSUPPORTED_CAMERA_TYPE = 501
    NETWORK_COULDNT_RESOLVE_HOST = 601
    NETWORK_COULDNT_CONNECT = 602
    NETWORK_OPERATION_TIMEDOUT = 603
    LPB_APP_OUT_OF_RANGE = 701
    LPB_APP_OUT_OF_MAXRANGE = 702
    LPB_APP_OUT_OF_MINRANGE = 703
    LPB_APP_MEMORY_ERROR = 704
    LPB_APP_READ_ONLY = 705
    LPB_APP_ILLEGAL_CMD = 706
    LPB_APP_VOID_DP = 707
    LPB_APP_TYPE_CONFLICT = 708
    LPB_APP_READ_CMD_INCORRECT = 709
    LPB_APP_WRITE_CMD_INCORRECT = 710
    LPB_APP_CMD_TYPE_INCORRECT = 711
    LPB_APP_WRITE_TIMEOUT = 712
    LPB_APP_CANNOT_WRITE_GW = 713
    LPB_APP_UNKNOWN_GATEWAY = 714
    LPB_APP_GATEWAY_UNREACHABLE = 715
    APPLICATION_ERROR = 800
    HUE_INVALID_CREDENTIALS = 900
    HUE_LINK_BUTTON_NOT_PRESSED = 901
    HUE_DEVICE_IS_OFF = 902
    TIMED_OUT = 10001
    CANCELLED = 10002
    UNKNOWN_ERROR_CODE = 10003
    SERVER_FAILURE = 10004
    PEER_DOWN = 10005
    GATEWAY_BUFFER_OVERFLOW = 10006
    UNKNOWN_DETAILED_ERROR = 10007

    @classmethod
    def _missing_(cls, value):  # type: ignore
        _LOGGER.warning(f"Unsupported value {value} has been returned for {cls}")
        return cls.UNKNOWN


@unique
class EventName(str, Enum):
    UNKNOWN = "Unknown"
    ACTION_GROUP_CREATED = "ActionGroupCreatedEvent"
    ACTION_GROUP_DELETED = "ActionGroupDeletedEvent"
    ACTION_GROUP_UPDATED = "ActionGroupUpdatedEvent"
    CALENDAR_DAY_CREATED = "CalendarDayCreatedEvent"
    CALENDAR_DAY_UPDATED = "CalendarDayUpdatedEvent"
    CALENDAR_RULE_CREATED = "CalendarRuleCreatedEvent"
    CALENDAR_RULE_DELETED = "CalendarRuleDeletedEvent"
    CAMERA_DISCOVERED = "CameraDiscoveredEvent"
    CAMERA_DISCOVER_FAILED = "CameraDiscoverFailedEvent"
    CAMERA_UPLOAD_PHOTO = "CameraUploadPhotoEvent"
    COMMAND_EXECUTION_STATE_CHANGE = "CommandExecutionStateChangedEvent"
    CONDITION_GROUP_CREATED = "ConditionGroupCreatedEvent"
    CONDITION_GROUP_DELETED = "ConditionGroupDeletedEvent"
    CONDITION_GROUP_UPDATED = "ConditionGroupUpdatedEvent"
    DELAYED_TRIGGER_CANCELLED = "DelayedTriggerCancelledEvent"
    DEVICE_AVAILABLE = "DeviceAvailableEvent"
    DEVICE_CREATED = "DeviceCreatedEvent"
    DEVICE_DELETION_FAILED = "DeviceDeletionFailedEvent"
    DEVICE_DISABLED = "DeviceDisabledEvent"
    DEVICE_FIRMWARE_UPDATE_FAILED = "DeviceFirmwareUpdateFailedEvent"
    DEVICE_PROTOCOL_AVAILABLE = "DeviceProtocolAvailableEvent"
    DEVICE_PROTOCOL_UNAVAILABLE = "DeviceProtocolUnavailableEvent"
    DEVICE_REMOVED = "DeviceRemovedEvent"
    DEVICE_STATE_CHANGED = "DeviceStateChangedEvent"
    DEVICE_UNAVAILABLE = "DeviceUnavailableEvent"
    DEVICE_UPDATED = "DeviceUpdatedEvent"
    DISCOVER_COMPLETE = "DiscoverCompleteEvent"
    DISCOVER_FAILED = "DiscoverFailedEvent"
    ELIOT_DISCOVER_GATEWAYS_COMPLETED = "EliotDiscoverGatewaysCompletedEvent"
    ELIOT_DISCOVER_GATEWAYS_FAILED = "EliotDiscoverGatewaysFailedEvent"
    ELIOT_DISCOVER_GATEWAY_COMPLETED = "EliotDiscoverGatewayCompletedEvent"
    ELIOT_DISCOVER_GATEWAY_FAILED = "EliotDiscoverGatewayFailedEvent"
    ELIOT_REFRESH_CURRENT_TOKEN_COMPLETED = "EliotRefreshCurrentTokenCompletedEvent"
    ELIOT_REFRESH_CURRENT_TOKEN_FAILED = "EliotRefreshCurrentTokenFailedEvent"
    END_USER_LOGIN = "EndUserLoginEvent"
    ENOCEAN_BAD_DEVICE_STIMULATION = "EnOceanBadDeviceStimulationEvent"
    ENOCEAN_KNOWN_DEVICE_FOUND = "EnOceanKnownDeviceFoundEvent"
    ENOCEAN_LEARN_STARTED = "EnOceanLearnStartedEvent"
    ENOCEAN_LEARN_STOPPED = "EnOceanLearnStoppedEvent"
    EXECUTION_REGISTERED = "ExecutionRegisteredEvent"
    EXECUTION_STATE_CHANGED = "ExecutionStateChangedEvent"
    GATEWAY_ALIVE = "GatewayAliveEvent"
    GATEWAY_BOOT = "GatewayBootEvent"
    GATEWAY_DOWN = "GatewayDownEvent"
    GATEWAY_FUNCTION_CHANGED = "GatewayFunctionChangedEvent"
    GATEWAY_MODE_CHANGED = "GatewayModeChangedEvent"
    GATEWAY_SYNCHRONIZATION_ENDED = "GatewaySynchronizationEndedEvent"
    GATEWAY_SYNCHRONIZATION_STARTED = "GatewaySynchronizationStartedEvent"
    INVALID_ADDRESS = "InvalidAddressEvent"
    IO_CHANGED_KEY = "IOChangedKeyEvent"
    OPENDOORS_DISCOVER_COMPLETED = "OpenDoorsDiscoverCompletedEvent"
    OPENDOORS_DISCOVER_FAILED = "OpenDoorsDiscoverFailedEvent"
    OPENDOORS_GENERATE_OAUTH_TOKENS_COMPLETED = (
        "OpenDoorsGenerateOAuthTokensCompletedEvent"
    )
    OPENDOORS_GENERATE_OAUTH_TOKENS_FAILED = "OpenDoorsGenerateOAuthTokensFailedEvent"
    PLACE_CREATED = "PlaceCreatedEvent"
    PLACE_DELETED = "PlaceDeletedEvent"
    PLACE_UPDATED = "PlaceUpdatedEvent"
    PURGE_PARTIAL_RAW_DEVICES = "PurgePartialRawDevicesEvent"
    REFRESH_ALL_DEVICES_STATES_COMPLETED = "RefreshAllDevicesStatesCompletedEvent"
    SETUP_JOB_COMPLETED = "SetupJobCompletedEvent"
    SETUP_JOB_FAILED = "SetupJobFailedEvent"
    SOMFY_PROTECT_GET_SITES_COMPLETED = "SomfyProtectGetSitesCompletedEvent"
    SONOS_GET_TOPOLOGY_SUCCESS = "SonosGetTopologySuccessEvent"
    TOKEN_CREATED = "TokenCreatedEvent"
    TOKEN_CREATION_FAILED = "TokenCreationFailedEvent"
    TOKEN_DELETION_FAILED = "TokenDeletionFailedEvent"
    TOKEN_REMOVED = "TokenRemovedEvent"
    VALID_ADDRESS = "ValidAddressEvent"
    ZIGBEE_BIND_NETWORK_COMPLETED = "ZigbeeBindNetworkCompletedEvent"
    ZIGBEE_BIND_NETWORK_FAILED = "ZigbeeBindNetworkFailedEvent"
    ZIGBEE_CREATE_NETWORK_COMPLETED = "ZigbeeCreateNetworkCompletedEvent"
    ZIGBEE_CREATE_NETWORK_FAILED = "ZigbeeCreateNetworkFailedEvent"
    ZIGBEE_JOIN_NETWORK_FAILED = "ZigbeeJoinNetworkFailedEvent"
    ZIGBEE_LEAVE_NETWORK_COMPLETED = "ZigbeeLeaveNetworkCompletedEvent"
    ZIGBEE_LEAVE_NETWORK_FAILED = "ZigbeeLeaveNetworkFailedEvent"
    ZIGBEE_REFRESH_NETWORK_COMPLETED = "ZigbeeRefreshNetworkCompletedEvent"

    @classmethod
    def _missing_(cls, value):  # type: ignore
        _LOGGER.warning(f"Unsupported value {value} has been returned for {cls}")
        return cls.UNKNOWN


@unique
class UpdateBoxStatus(str, Enum):
    NOT_UPDATABLE = "NOT_UPDATABLE"
    READY_TO_UPDATE = "READY_TO_UPDATE"
    READY_TO_BE_UPDATED_BY_SERVER = "READY_TO_BE_UPDATED_BY_SERVER"
    READY_TO_UPDATE_LOCALLY = "READY_TO_UPDATE_LOCALLY"
    UP_TO_DATE = "UP_TO_DATE"
    UNKNOWN = "UNKNOWN"
    UPDATING = "UPDATING"


@unique
class CommandMode(str, Enum):
    HIGH_PRIORITY = "highPriority"
    GEOLOCATED = "geolocated"
    INTERNAL = "internal"


@unique
class UiWidget(str, Enum):
    # From /reference/ui/widgets
    AIR_FLOW_SENSOR = "AirFlowSensor"
    AIR_QUALITY_SENSOR = "AirQualitySensor"
    ALARM_PANEL_CONTROLLER = "AlarmPanelController"
    ALARM_REMOTE_CONTROLLER = "AlarmRemoteController"
    ATLANTIC_ELECTRICAL_HEATER = "AtlanticElectricalHeater"
    ATLANTIC_ELECTRICAL_HEATER_WITH_ADJUSTABLE_TEMPERATURE_SETPOINT = (
        "AtlanticElectricalHeaterWithAdjustableTemperatureSetpoint"
    )
    ATLANTIC_ELECTRICAL_TOWEL_DRYER = "AtlanticElectricalTowelDryer"
    ATLANTIC_HEAT_RECOVERY_VENTILATION = "AtlanticHeatRecoveryVentilation"
    ATLANTIC_MULTI_METER_ELECTRIC_CONFIGURATION = (
        "AtlanticMultiMeterElectricConfiguration"
    )
    ATLANTIC_MULTI_METER_ELECTRIC_HEAT_PUMP = "AtlanticMultiMeterElectricHeatPump"
    ATLANTIC_MULTI_METER_ELECTRIC_SENSOR = "AtlanticMultiMeterElectricSensor"
    ATLANTIC_PASS_APCBOILER = "AtlanticPassAPCBoiler"
    ATLANTIC_PASS_APCDHW = "AtlanticPassAPCDHW"
    ATLANTIC_PASS_APCHEAT_PUMP = "AtlanticPassAPCHeatPump"
    ATLANTIC_PASS_APCHEATING_AND_COOLING_ZONE = "AtlanticPassAPCHeatingAndCoolingZone"
    ATLANTIC_PASS_APCHEATING_ZONE = "AtlanticPassAPCHeatingZone"
    ATLANTIC_PASS_APCZONE_CONTROL = "AtlanticPassAPCZoneControl"
    AWNING_VALANCE = "AwningValance"
    BALLAST = "Ballast"
    BATTERY_SENSOR = "BatterySensor"
    BIOCLIMATIC_PERGOLA = "BioclimaticPergola"
    CO_2_SENSOR = "CO2Sensor"
    COSENSOR = "COSensor"
    CAR_BUTTON_SENSOR = "CarButtonSensor"
    CAR_LOCK = "CarLock"
    CARD_SWITCH = "CardSwitch"
    CIRCUIT_BREAKER = "CircuitBreaker"
    CONTACT_SENSOR = "ContactSensor"
    COTHERM_THERMOSTAT = "CothermThermostat"
    CUMULATIVE_ELECTRIC_POWER_CONSUMPTION_SENSOR = (
        "CumulativeElectricPowerConsumptionSensor"
    )
    CUMULATIVE_ELECTRIC_POWER_PRODUCTION_SENSOR = (
        "CumulativeElectricPowerProductionSensor"
    )
    CUMULATIVE_FOSSIL_ENERGY_CONSUMPTION_SENSOR = (
        "CumulativeFossilEnergyConsumptionSensor"
    )
    CUMULATIVE_GAS_CONSUMPTION_SENSOR = "CumulativeGasConsumptionSensor"
    CUMULATIVE_THERMAL_ENERGY_CONSUMPTION_SENSOR = (
        "CumulativeThermalEnergyConsumptionSensor"
    )
    CUMULATIVE_WATER_CONSUMPTION_SENSOR = "CumulativeWaterConsumptionSensor"
    CURTAIN_TRACK_UNO = "CurtainTrackUno"
    CYCLIC_GENERIC = "CyclicGeneric"
    DHWSET_POINT = "DHWSetPoint"
    DE_DIETRICH_BOILER = "DeDietrichBoiler"
    DE_DIETRICH_DHW = "DeDietrichDHW"
    DE_DIETRICH_HEATING_CIRCUIT = "DeDietrichHeatingCircuit"
    DE_DIETRICH_MODBUS_GATEWAY = "DeDietrichModbusGateway"
    DE_DIETRICH_SWIMMING_POOL = "DeDietrichSwimmingPool"
    DIMMER_CIECOLOR_SPACE_XYLIGHT = "DimmerCIEColorSpaceXYLight"
    DIMMER_COLOR_TEMPERATURE_LIGHT = "DimmerColorTemperatureLight"
    DIMMER_EXTERIOR_HEATING = "DimmerExteriorHeating"
    DIMMER_HUE_SAT_OR_CTLIGHT = "DimmerHueSatOrCTLight"
    DIMMER_HUE_SATURATION_LIGHT = "DimmerHueSaturationLight"
    DIMMER_LIGHT = "DimmerLight"
    DIMMER_ON_OFF = "DimmerOnOff"
    DIMMER_ON_OFF_LIGHT = "DimmerOnOffLight"
    DIMMER_RGBCOLOURED_LIGHT = "DimmerRGBColouredLight"
    DIMPLEX_VENTILATION_INLET_OUTLET = "DimplexVentilationInletOutlet"
    DISCRETE_EXTERIOR_HEATING = "DiscreteExteriorHeating"
    DISCRETE_POSITIONABLE_GARAGE_DOOR = "DiscretePositionableGarageDoor"
    DISCRETE_POSITIONABLE_GATE = "DiscretePositionableGate"
    DOCK = "Dock"
    DOMESTIC_HOT_WATER_PRODUCTION = "DomesticHotWaterProduction"
    DOMESTIC_HOT_WATER_TANK = "DomesticHotWaterTank"
    DOOR_LOCK = "DoorLock"
    DROP_ARM_AWNING = "DropArmAwning"
    DYNAMIC_AIR_VENT = "DynamicAirVent"
    DYNAMIC_ALARM = "DynamicAlarm"
    DYNAMIC_AWNING = "DynamicAwning"
    DYNAMIC_BRIDGE = "DynamicBridge"
    DYNAMIC_CIRCUIT_BREAKER = "DynamicCircuitBreaker"
    DYNAMIC_CURTAIN = "DynamicCurtain"
    DYNAMIC_GARAGE_DOOR = "DynamicGarageDoor"
    DYNAMIC_GATE = "DynamicGate"
    DYNAMIC_GATEWAY = "DynamicGateway"
    DYNAMIC_HEATER = "DynamicHeater"
    DYNAMIC_HUMIDITY_SENSOR = "DynamicHumiditySensor"
    DYNAMIC_HVAC_CENTRAL_UNIT = "DynamicHvacCentralUnit"
    DYNAMIC_INTRUSION_SENSOR = "DynamicIntrusionSensor"
    DYNAMIC_LIGHT = "DynamicLight"
    DYNAMIC_LIGHT_SENSOR = "DynamicLightSensor"
    DYNAMIC_OCCUPANCY_SENSOR = "DynamicOccupancySensor"
    DYNAMIC_OPENING_SENSOR = "DynamicOpeningSensor"
    DYNAMIC_OUTLET = "DynamicOutlet"
    DYNAMIC_OVEN = "DynamicOven"
    DYNAMIC_PERGOLA = "DynamicPergola"
    DYNAMIC_RAIN_SENSOR = "DynamicRainSensor"
    DYNAMIC_SCREEN = "DynamicScreen"
    DYNAMIC_SHUTTER = "DynamicShutter"
    DYNAMIC_TEMPERATURE_SENSOR = "DynamicTemperatureSensor"
    DYNAMIC_THERMOSTAT = "DynamicThermostat"
    DYNAMIC_THIRD_PARTY_GATEWAY = "DynamicThirdPartyGateway"
    DYNAMIC_VENETIAN_BLIND = "DynamicVenetianBlind"
    DYNAMIC_VENTILATION = "DynamicVentilation"
    DYNAMIC_WASHING_MACHINE = "DynamicWashingMachine"
    DYNAMIC_WEATHER_STATION = "DynamicWeatherStation"
    DYNAMIC_WIND_SENSOR = "DynamicWindSensor"
    DYNAMIC_WINDOW = "DynamicWindow"
    ELECTRICAL_HEATER = "ElectricalHeater"
    ELECTRICAL_HEATER_WITH_ADJUSTABLE_TEMPERATURE_SETPOINT = (
        "ElectricalHeaterWithAdjustableTemperatureSetpoint"
    )
    EMPTY_REMOTE_CONTROLLER = "EmptyRemoteController"
    EN_OCEAN_GENERIC = "EnOceanGeneric"
    EN_OCEAN_GENERIC_ELECTRIC_COUNTER = "EnOceanGenericElectricCounter"
    EN_OCEAN_TRANSCEIVER = "EnOceanTransceiver"
    EVO_HOME_CONTROLLER = "EvoHomeController"
    EWATTCH_TICCOUNTER = "EwattchTICCounter"
    EXTERIOR_VENETIAN_BLIND = "ExteriorVenetianBlind"
    FLOOR_HEATING = "FloorHeating"
    GAS_DHWCONSUMPTION_SENSOR = "GasDHWConsumptionSensor"
    GAS_HEATER_CONSUMPTION_SENSOR = "GasHeaterConsumptionSensor"
    GENERIC_16_CHANNELS_COUNTER = "Generic16ChannelsCounter"
    GENERIC_1_CHANNEL_COUNTER = "Generic1ChannelCounter"
    GENERIC_CAMERA = "GenericCamera"
    GROUP_CONFIGURATION = "GroupConfiguration"
    HEAT_DETECTION_SENSOR = "HeatDetectionSensor"
    HEAT_PUMP = "HeatPump"
    HEATING_SET_POINT = "HeatingSetPoint"
    HEATING_TEMPERATURE_INTERFACE = "HeatingTemperatureInterface"
    HITACHI_AIR_TO_AIR_HEAT_PUMP = "HitachiAirToAirHeatPump"
    HITACHI_AIR_TO_WATER_HEATING_ZONE = "HitachiAirToWaterHeatingZone"
    HITACHI_AIR_TO_WATER_MAIN_COMPONENT = "HitachiAirToWaterMainComponent"
    HITACHI_DHW = "HitachiDHW"
    HITACHI_SWIMMING_POOL = "HitachiSwimmingPool"
    HITACHI_THERMOSTAT = "HitachiThermostat"
    HOMEKIT_STACK = "HomekitStack"
    HUE_BRIDGE = "HueBridge"
    IOGENERIC = "IOGeneric"
    IOSIREN = "IOSiren"
    IOSTACK = "IOStack"
    IRBLASTER = "IRBlaster"
    IMHOTEP_HEATING_TEMPERATURE_INTERFACE = "ImhotepHeatingTemperatureInterface"
    INSTANT_ELECTRIC_CURRENT_CONSUMPTION_SENSOR = (
        "InstantElectricCurrentConsumptionSensor"
    )
    INSTANT_ELECTRIC_POWER_CONSUMPTION_SENSOR = "InstantElectricPowerConsumptionSensor"
    INTRUSION_DETECTOR = "IntrusionDetector"
    INTRUSION_EVENT_SENSOR = "IntrusionEventSensor"
    INTRUSION_SENSOR = "IntrusionSensor"
    INVALID = "Invalid"
    JSWCAMERA = "JSWCamera"
    KIZ_OTHERM_BRIDGE = "KizOThermBridge"
    KIZ_OTHERM_V_2_BRIDGE = "KizOThermV2Bridge"
    LOCK_UNLOCK_DOOR_LOCK_WITH_UNKNOWN_POSITION = (
        "LockUnlockDoorLockWithUnknownPosition"
    )
    LUMINANCE_SENSOR = "LuminanceSensor"
    MEDIA_RENDERER = "MediaRenderer"
    MOTION_SENSOR = "MotionSensor"
    MULTI_METER_ELECTRIC_SENSOR = "MultiMeterElectricSensor"
    MY_FOX_ALARM_CONTROLLER = "MyFoxAlarmController"
    MY_FOX_CAMERA = "MyFoxCamera"
    MY_FOX_SECURITY_CAMERA = "MyFoxSecurityCamera"
    NODE = "Node"
    OVPGENERIC = "OVPGeneric"
    OCCUPANCY_SENSOR = "OccupancySensor"
    ON_OFF_HEATING_SYSTEM = "OnOffHeatingSystem"
    ON_OFF_LIGHT = "OnOffLight"
    ON_OFF_REMOTECONTROLLER = "OnOffRemotecontroller"
    OPEN_CLOSE_GATE = "OpenCloseGate"
    OPEN_CLOSE_GATE_4_T = "OpenCloseGate4T"
    OPEN_CLOSE_GATE_WITH_PEDESTRIAN_POSITION = "OpenCloseGateWithPedestrianPosition"
    OPEN_CLOSE_SLIDING_GARAGE_DOOR = "OpenCloseSlidingGarageDoor"
    OPEN_CLOSE_SLIDING_GARAGE_DOOR_4_T = "OpenCloseSlidingGarageDoor4T"
    OPEN_CLOSE_SLIDING_GARAGE_DOOR_WITH_PEDESTRIAN_POSITION = (
        "OpenCloseSlidingGarageDoorWithPedestrianPosition"
    )
    OPEN_CLOSE_SLIDING_GATE = "OpenCloseSlidingGate"
    OPEN_CLOSE_SLIDING_GATE_4_T = "OpenCloseSlidingGate4T"
    OPEN_CLOSE_SLIDING_GATE_WITH_PEDESTRIAN_POSITION = (
        "OpenCloseSlidingGateWithPedestrianPosition"
    )
    OPEN_THERM_DIAGNOSTIC = "OpenThermDiagnostic"
    PERGOLA_HORIZONTAL_AWNING = "PergolaHorizontalAwning"
    PERGOLA_HORIZONTAL_AWNING_UNO = "PergolaHorizontalAwningUno"
    PERGOLA_SIDE_SCREEN = "PergolaSideScreen"
    POD = "Pod"
    POSITIONABLE_AND_LOCKABLE_SLIDING_WINDOW = "PositionableAndLockableSlidingWindow"
    POSITIONABLE_AND_STRETCHABLE_PERGOLA_SCREEN = (
        "PositionableAndStretchablePergolaScreen"
    )
    POSITIONABLE_CURTAIN = "PositionableCurtain"
    POSITIONABLE_DUAL_ROLLER_SHUTTER = "PositionableDualRollerShutter"
    POSITIONABLE_EXTERIOR_VENETIAN_BLIND = "PositionableExteriorVenetianBlind"
    POSITIONABLE_EXTERIOR_VENETIAN_BLIND_UNO = "PositionableExteriorVenetianBlindUno"
    POSITIONABLE_EXTERIOR_VENETIAN_BLIND_WITH_WP = (
        "PositionableExteriorVenetianBlindWithWP"
    )
    POSITIONABLE_EXTERIOR_VENETIAN_BLIND_WITH_WP_2 = (
        "PositionableExteriorVenetianBlindWithWP2"
    )
    POSITIONABLE_GARAGE_DOOR = "PositionableGarageDoor"
    POSITIONABLE_GARAGE_DOOR_WITH_PARTIAL_POSITION = (
        "PositionableGarageDoorWithPartialPosition"
    )
    POSITIONABLE_GATE = "PositionableGate"
    POSITIONABLE_GATE_WITH_PEDESTRIAN_POSITION = (
        "PositionableGateWithPedestrianPosition"
    )
    POSITIONABLE_HORIZONTAL_AWNING = "PositionableHorizontalAwning"
    POSITIONABLE_HORIZONTAL_AWNING_UNO = "PositionableHorizontalAwningUno"
    POSITIONABLE_OR_ORIENTABLE_ROLLER_SHUTTER = "PositionableOrOrientableRollerShutter"
    POSITIONABLE_OR_PROGRESSIVE_ORIENTABLE_ROLLER_SHUTTER = (
        "PositionableOrProgressiveOrientableRollerShutter"
    )
    POSITIONABLE_PROJECTION_ROLLER_SHUTTER = "PositionableProjectionRollerShutter"
    POSITIONABLE_ROLLER_SHUTTER = "PositionableRollerShutter"
    POSITIONABLE_ROLLER_SHUTTER_UNO = "PositionableRollerShutterUno"
    POSITIONABLE_ROLLER_SHUTTER_WITH_LOW_SPEED_MANAGEMENT = (
        "PositionableRollerShutterWithLowSpeedManagement"
    )
    POSITIONABLE_SCREEN = "PositionableScreen"
    POSITIONABLE_SCREEN_UNO = "PositionableScreenUno"
    POSITIONABLE_SLIDING_WINDOW = "PositionableSlidingWindow"
    POSITIONABLE_TILTED_ROLLER_SHUTTER = "PositionableTiltedRollerShutter"
    POSITIONABLE_TILTED_SCREEN = "PositionableTiltedScreen"
    POSITIONABLE_TILTED_WINDOW = "PositionableTiltedWindow"
    POSITIONABLE_VENETIAN_BLIND = "PositionableVenetianBlind"
    POSITIONABLE_WINDOW = "PositionableWindow"
    POSITIONABLE_WINDOW_UNO = "PositionableWindowUno"
    PROGRAMMABLE_AND_PROTECTABLE_THERMOSTAT_SET_POINT = (
        "ProgrammableAndProtectableThermostatSetPoint"
    )
    RTDINDOOR_SIREN = "RTDIndoorSiren"
    RTDOUTDOOR_SIREN = "RTDOutdoorSiren"
    RTSGENERIC = "RTSGeneric"
    RTSGENERIC_4_T = "RTSGeneric4T"
    RTSTHERMOSTAT = "RTSThermostat"
    RAIN_SENSOR = "RainSensor"
    RELATIVE_HUMIDITY_SENSOR = "RelativeHumiditySensor"
    REMOTE_CONTROLLER_ONE_WAY = "RemoteControllerOneWay"
    REPEATER = "Repeater"
    ROCKER_SWITCH_AUTO_MANU_UP_DOWN_CONTROLLER = "RockerSwitchAutoManuUpDownController"
    ROCKER_SWITCHX_1_CONTROLLER = "RockerSwitchx1Controller"
    ROCKER_SWITCHX_2_CONTROLLER = "RockerSwitchx2Controller"
    ROCKER_SWITCHX_4_CONTROLLER = "RockerSwitchx4Controller"
    SCENE_CONTROLLER = "SceneController"
    SCHNEIDER_SWITCH_CONFIGURATION = "SchneiderSwitchConfiguration"
    SIREN_STATUS = "SirenStatus"
    SLATS_ORIENTATION = "SlatsOrientation"
    SLIDING_DISCRETE_GATE_WITH_PEDESTRIAN_POSITION = (
        "SlidingDiscreteGateWithPedestrianPosition"
    )
    SMOKE_SENSOR = "SmokeSensor"
    SOMFY_CONFIGURATION_TOOL = "SomfyConfigurationTool"
    SOMFY_HEATING_TEMPERATURE_INTERFACE = "SomfyHeatingTemperatureInterface"
    SOMFY_PILOT_WIRE_ELECTRICAL_HEATER = "SomfyPilotWireElectricalHeater"
    SOMFY_PILOT_WIRE_HEATING_INTERFACE = "SomfyPilotWireHeatingInterface"
    SOMFY_THERMOSTAT = "SomfyThermostat"
    STATEFUL_ALARM_CONTROLLER = "StatefulAlarmController"
    STATEFUL_ON_OFF = "StatefulOnOff"
    STATEFUL_ON_OFF_LIGHT = "StatefulOnOffLight"
    STATELESS_ALARM_CONTROLLER = "StatelessAlarmController"
    STATELESS_EXTERIOR_HEATING = "StatelessExteriorHeating"
    STATELESS_ON_OFF = "StatelessOnOff"
    SUN_ENERGY_SENSOR = "SunEnergySensor"
    SUN_INTENSITY_SENSOR = "SunIntensitySensor"
    SWIMMING_POOL = "SwimmingPool"
    SWINGING_SHUTTER = "SwingingShutter"
    TSKALARM_CONTROLLER = "TSKAlarmController"
    TEMPERATURE_SENSOR = "TemperatureSensor"
    THERMOSTAT_HEATING_TEMPERATURE_INTERFACE = "ThermostatHeatingTemperatureInterface"
    THERMOSTAT_SET_POINT = "ThermostatSetPoint"
    THERMOSTAT_ZONES_CONTROLLER = "ThermostatZonesController"
    THREE_WAY_WINDOW_HANDLE = "ThreeWayWindowHandle"
    TILT_ONLY_VENETIAN_BLIND = "TiltOnlyVenetianBlind"
    TIMED_ON_OFF = "TimedOnOff"
    TIMED_ON_OFF_LIGHT = "TimedOnOffLight"
    UNIVERSAL_SENSOR = "UniversalSensor"
    UNTYPED = "Untyped"
    UP_DOWN_BIOCLIMATIC_PERGOLA = "UpDownBioclimaticPergola"
    UP_DOWN_CELLULAR_SCREEN = "UpDownCellularScreen"
    UP_DOWN_CURTAIN = "UpDownCurtain"
    UP_DOWN_DUAL_CURTAIN = "UpDownDualCurtain"
    UP_DOWN_EXTERIOR_SCREEN = "UpDownExteriorScreen"
    UP_DOWN_EXTERIOR_VENETIAN_BLIND = "UpDownExteriorVenetianBlind"
    UP_DOWN_GARAGE_DOOR = "UpDownGarageDoor"
    UP_DOWN_GARAGE_DOOR_4_T = "UpDownGarageDoor4T"
    UP_DOWN_GARAGE_DOOR_WITH_VENTILATION_POSITION = (
        "UpDownGarageDoorWithVentilationPosition"
    )
    UP_DOWN_HORIZONTAL_AWNING = "UpDownHorizontalAwning"
    UP_DOWN_ROLLER_SHUTTER = "UpDownRollerShutter"
    UP_DOWN_SCREEN = "UpDownScreen"
    UP_DOWN_SHEER_SCREEN = "UpDownSheerScreen"
    UP_DOWN_SWINGING_SHUTTER = "UpDownSwingingShutter"
    UP_DOWN_VENETIAN_BLIND = "UpDownVenetianBlind"
    UP_DOWN_WINDOW = "UpDownWindow"
    UP_DOWN_ZEBRA_SCREEN = "UpDownZebraScreen"
    VOCSENSOR = "VOCSensor"
    VALVE_HEATING_TEMPERATURE_INTERFACE = "ValveHeatingTemperatureInterface"
    VENTILATION_INLET = "VentilationInlet"
    VENTILATION_OUTLET = "VentilationOutlet"
    VENTILATION_TRANSFER = "VentilationTransfer"
    WATER_DETECTION_SENSOR = "WaterDetectionSensor"
    WEATHER_FORECAST_SENSOR = "WeatherForecastSensor"
    WIFI = "Wifi"
    WIND_SPEED_SENSOR = "WindSpeedSensor"
    WINDOW_LOCK = "WindowLock"
    WINDOW_WITH_TILT_SENSOR = "WindowWithTiltSensor"
    ZWAVE_AEOTEC_CONFIGURATION = "ZWaveAeotecConfiguration"
    ZWAVE_CONFIGURATION = "ZWaveConfiguration"
    ZWAVE_DANFOSS_RSLINK = "ZWaveDanfossRSLink"
    ZWAVE_DOOR_LOCK_CONFIGURATION = "ZWaveDoorLockConfiguration"
    ZWAVE_FIBARO_ROLLER_SHUTTER_CONFIGURATION = "ZWaveFibaroRollerShutterConfiguration"
    ZWAVE_HEATIT_THERMOSTAT_CONFIGURATION = "ZWaveHeatitThermostatConfiguration"
    ZWAVE_NODON_CONFIGURATION = "ZWaveNodonConfiguration"
    ZWAVE_QUBINO_CONFIGURATION = "ZWaveQubinoConfiguration"
    ZWAVE_SEDEVICE_CONFIGURATION = "ZWaveSEDeviceConfiguration"
    ZWAVE_TRANSCEIVER = "ZWaveTransceiver"
    ZIGBEE_NETWORK = "ZigbeeNetwork"
    ZIGBEE_STACK = "ZigbeeStack"
