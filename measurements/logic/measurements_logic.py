from ..models import Measurement
from ..models import Variable
from variables.logic import variables_logic as vl
def get_measurements():
    measurements = Measurement.objects.all()
    return measurements

def get_measurement(var_pk):
    measurement = Measurement.objects.get(pk=var_pk)
    return measurement

def update_measurement(var_pk, new_var):
    measurement = get_measurement(var_pk)
    measurement.value = new_var["value"]
    measurement.unit=new_var["unit"]
    measurement.place=new_var["place"]
    measurement.save()
    return measurement

def create_measurement(mea):
    measurement = Measurement(variable_id = mea["variable_id"], value = mea["value"], unit=mea["unit"], place=mea["place"] )
    measurement.save()
    return measurement
   