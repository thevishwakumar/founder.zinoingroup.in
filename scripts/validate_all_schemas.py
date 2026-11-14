import os
import json
import jsonschema

schemas = {
    'profile.json': 'profile.schema.json',
    'expertise.json': 'expertise.schema.json',
    'projects.json': 'projects.schema.json',
    'experience.json': 'experience.schema.json',
    'education.json': 'education.schema.json',
    'certifications.json': 'certifications.schema.json',
    'social-links.json': 'social-links.schema.json'
}

data_dir = os.path.join('founder.zinoingroup.in', 'data')
schema_dir = os.path.join(data_dir, 'schemas')

for d_file, s_file in schemas.items():
    d_path = os.path.join(data_dir, d_file)
    s_path = os.path.join(schema_dir, s_file)
    with open(d_path, 'r', encoding='utf-8') as df:
        data = json.load(df)
    with open(s_path, 'r', encoding='utf-8') as sf:
        schema = json.load(sf)
    try:
        jsonschema.validate(instance=data, schema=schema)
        print(f"[VALID] {d_file} matches {s_file}")
    except Exception as e:
        print(f"[INVALID] {d_file}: {e.message}")
