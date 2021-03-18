# config
# To manage the configuration for the monitor function
# including 
# - generate default config, 
# - load the config from the config file


import json
import os


_CFG_FILE_NAME = 'config.json'

_DEF_CFG = {
    'kafka' : {
        ## For local debugging (local kafka server)
        # 'broker':'127.0.0.1:9092',  # plantext: 'localhost:9092',  ssl: 'localhost:9093'
        # 'sec_protocol':'PLAINTEXT',
        # 'ssl_ca':'ca.pem',
        # 'ssl_cert':'service.cert',
        # 'ssl_key':'service.key',
        # 'topic':'topic-web-mon',

        ## for cloud service
        'broker':'kafka-1523402e-jerry-cffe.aivencloud.com:13430',
        'sec_protocol':'SSL',
        'ssl_ca':'ca.pem',
        'ssl_cert':'service.cert',
        'ssl_key':'service.key',
        'topic':'topic-web-mon',
    },
    'db': {
        ## For local debugging (local postgresql DB)
        # 'host':'127.0.0.1',
        # 'port':'5432',
        # 'user':'webmon_user',
        # 'password':'webmon_pwd',
        # 'database':'webmon_db',
        # 'table':'webmon_records'

        ## For cloud service
        'host':'psql-service-xy-jerry-cffe.aivencloud.com',
        'port':'13428',
        'user':'avnadmin',
        'password':'tdzaa56ioi3df2fy',
        'database':'defaultdb',
        'table':'webmon_records'
    },
    'webmon' : [
        {
            'url':'http://kafka.apache.org/',
            'pattern':r'<title>Apache\s*Kafka</title>',
            'interval':30,
        },
        {
            'url':'https://console.aiven.io/signup.html',
            'pattern':r'\(window\.location\.hostname\.match\(\"aiven\.io\"\)\)',
            'interval':20,
        },
        # more website config...
    ],
}


class ConfigError(Exception):
    """Base exception for general config error"""
    pass


class ConfigOprError(ConfigError):
    """Config file operation error"""
    pass


class LoadCfgError(ConfigError):
    """Load configuration error"""
    pass


class WebMonConfig(object):
    def __init__(self) -> None:
        self._cfg = None
        self._def_cfgfile = None
        if not self._def_cfgfile_exist():
            self._gen_cfgfile()

    def _gen_cfgfile(self, overwrite=False) -> None:
        global _DEF_CFG
        jcfg = json.dumps(_DEF_CFG)
        if self._def_cfgfile_exist() and not overwrite:
            return
        try:
            with open(self._default_cfgfile(), mode='w+') as f:
                f.write(jcfg)
        except Exception as e:
            raise ConfigOprError(f'Error writing default config file: {e}')

    def _default_cfgfile(self) -> str:
        global _CFG_FILE_NAME
        if not self._def_cfgfile:
            cwd = os.getcwd()
            self._def_cfgfile = os.path.join(cwd, _CFG_FILE_NAME)
        return self._def_cfgfile

    def _def_cfgfile_exist(self) -> bool:
        """Check if the default config file exist
        
        Return:
          True if default config file exist, otherwise False
        """
        return os.path.exists(self._default_cfgfile())

    def _load_config(self):
        """Load the configuration from the config file.
           If config file not found, load the default configuration.

        Raise: 
          LoadCfgError if failed to load the config
        """
        global _DEF_CFG
        if self._def_cfgfile_exist():
            try:
                with open(self._default_cfgfile(), mode='rt') as f:
                    self._cfg = json.load(f)
            except Exception as e:
                raise LoadCfgError(f'Failed loading the configuration: {e}')
        else:
            self._cfg = _DEF_CFG

    def config(self) -> dict:
        """Get the configuration.

        Return:
          a dict() for the configuration
        """
        if not self._cfg:
            self._load_config()
        return self._cfg
