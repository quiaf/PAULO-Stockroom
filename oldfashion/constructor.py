# Definicion de clases
class Device:
  def __init__(self, model, manufacturer, atype):
    self.model = model
    self.manufacturer = manufacturer
    self.atype = atype
    
    
class Stockroom:
  def __init__(self, name, address):
    self.name = name
    self.address = address
    
    
class Person:
  def __init__(self, name, last_name, mobile, dni, password, role):
    self.name = name
    self.last_name = last_name
    self.mobile = mobile
    self.dni = dni
    self.password = password
    self.role = role    
    
class DeviceStockroom:
  def __init__(self, quantity, stockroom, device):
    self.quantity = quantity
    self.stockroom = stockroom
    self.device = device    
    
class Manager:
    pass
        
    
class Owner:
    pass
    
class location:
  def __init__(self, country, state, neighborhood):
    self.name = name
    self.state = state
    self.neighborhood = neighborhood   

