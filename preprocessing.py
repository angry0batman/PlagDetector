import re

def preprocess_code(code):
    # Remove comments
    code = re.sub(r'//.*', '', code)  # Remove single line comments
    code = re.sub(r'/\*.*?\*/', '', code, flags=re.DOTALL)  # Remove multi-line comments
    
    # Normalize whitespace
    code = re.sub(r'\s+', ' ', code).strip()
    
    # Remove newlines
    code = code.replace('\n', ' ')
    
    return code
