import json
import yaml


MAPPING = {
  '.json': json.load,
  '.yaml': yaml.safe_load,
  '.yml': yaml.safe_load,
}
