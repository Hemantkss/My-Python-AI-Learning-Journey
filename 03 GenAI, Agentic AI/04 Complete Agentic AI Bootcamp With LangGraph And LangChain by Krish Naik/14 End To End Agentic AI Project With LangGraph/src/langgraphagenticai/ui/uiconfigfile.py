from configparser import ConfigParser


# Read configuration from the INI file
class Config:
    # Initialize with the path to the configuration file
    def __init__(self, config_file='./src/langgraphagenticai/ui/uiconfigfile.ini'):
        self.config = ConfigParser()
        self.config.read(config_file)
        
    # Get specific configuration values
    def get_llm_options(self):
        return self.config["DEFAULT"].get("LLM_OPTIONS").split(', ')

    def get_usecase_options(self):
        return self.config["DEFAULT"].get("USECASE_OPTIONS").split(', ')
    
    def get_openai_model_options(self):
        return self.config["DEFAULT"].get("OPENAI_MODEL_OPTIONS").split(', ')
    
    def get_page_title(self):
        return self.config["DEFAULT"].get("PAGE_TITLE")