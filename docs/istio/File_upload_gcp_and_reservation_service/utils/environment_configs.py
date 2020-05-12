import yaml

class EnvironmentConfigs:
    with open("/opt/config.yaml", 'r') as stream:
        yaml_con = yaml.safe_load(stream)

        logfile_path = yaml_con['DEFAULT']['LogFilePath']
        log_level = yaml_con['DEFAULT']['LogLevel']
        django_settings_debug = yaml_con['DEFAULT']['SettingsDebugFlag']

        mongo_server_ip = yaml_con['MONGO']['ServerIP']
        mongo_server_port = yaml_con['MONGO']['ServerPort']
        mongo_database = yaml_con['MONGO']['Database']
        mongo_roles_collection = yaml_con['MONGO']['RolesCollection']
        mongo_users_collection = yaml_con['MONGO']['UserCollection']
        mongo_reserved_ips_collection = yaml_con['MONGO']['ReservedIPCollection']
        mongo_audit_logs_collection = yaml_con['MONGO']['AuditLogCollection']

        infoblox_url = yaml_con['INFOBLOX']['InfobloxURL']
        infoblox_username = yaml_con['INFOBLOX']['InfobloxUsername']
        infoblox_password = yaml_con['INFOBLOX']['InfobloxPassword']

        admin_roles = yaml_con['ROLES']['AdminRoles']
        user_roles = yaml_con['ROLES']['UserRoles']