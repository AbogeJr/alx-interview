#!/usr/bin/python3
"""
UTF-8 validation
"""

def validUTF8(data):
    """
    method that determines if a given data set
    represents a valid UTF-8 encoding
    """
    remaining_bytes = 0
    
    for byte in data:
        if remaining_bytes > 0:
            if (byte >> 6) != 0b10:
                return False
            remaining_bytes -= 1
        else:
            if byte >> 7 == 0:
                remaining_bytes = 0 
            elif byte >> 5 == 0b110:
                remaining_bytes = 1 
            elif byte >> 4 == 0b1110:
                remaining_bytes = 2 
            elif byte >> 3 == 0b11110:
                remaining_bytes = 3 
            else:
                return False
        
    return remaining_bytes == 0

