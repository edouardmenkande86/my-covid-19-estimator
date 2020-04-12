import math

def estimator(data):
    data = {
        'region': {
            'name': "Africa",
            'avgAge': 19.7,
            'avgDailyIncomeInUSD': 5,
            'avgDailyIncomePopulation': 0.71
        },
        'periodeType':'days',
        'timeToElapse': 58,
        'reportedCases': 674,
        'population': 66622705,
        'totalHospitalBeds': 1380614
    }
   
    return data

# challenge 1

def covid19ImpactEstimator(data):

    estimate = {
        "impact": {
            'currentlyInfected': data.get('reportedCases') * 10
        },
        "severeImpact": {
            'currentlyInfected': data.get('reportedCases') * 50
        }
    }
    if data['periodeType'] == 'days':
        periodTime = data.get('timeToElapse')

        estimate = {
            "impact": {
                'currentlyInfected': data.get('reportedCases') * 10,
                'infectionsByRequestedTime': estimate.get('impact').get('currentlyInfected') * 18,
                'severeCasesByRequestedTime': estimate.get('impact').get('infectionByRequestedTime') * 0.15,
                'hospitalBedsByRequestedTime': data.get('totalHospitalBeds')*0.35 - estimate.get('impact').get(
                    'severeCasesByRequestedTime'),
                'casesForICUByRequestedTime': estimate.get('impact').get('infectionsByRequestedTime') * 0.05,
                'casesForVentilatorsByRequestedTime': estimate.get('impact').get('infectionsByRequestedTime') * 0.02,
                'dollarsInFlight': math.trunc((estimate.get('infectionsByRequestedTime')
                                               * data.get('region').get('avgDailyIncomePopulation')
                                               * data.get('region').get)/periodTime)

            },
            "severeImpact": {
                'currentlyInfected': data.get('reportedCases') * 50,
                'infectionsByRequestedTime': estimate.get('severeImpact').get('currentlyInfected') * 18,
                'severeCasesByRequestedTime': estimate.get('severeImpact').get('infectionByRequestedTime') * 0.15,
                'hospitalBedsByRequestedTime': data.get('totalHospitalBeds')*0.35 - estimate.get('severeImpact').get(
                    'severeCasesByRequestedTime'),
                'casesForICUByRequestedTime': estimate.get('severeImpact').get('infectionsByRequestedTime') * 0.05,
                'casesForVentilatorsByRequestedTime': estimate.get('severeImpact').get('infectionsByRequestedTime') * 0.02,
                'dollarsInFlight': math.trunc((estimate.get('infectionsByRequestedTime')
                                               * data.get('region').get('avgDailyIncomePopulation')
                                               * data.get('region').get) / periodTime)
            }

        }
    elif data['periodeType'] == 'weeks':
        periodTime = data.get('timeToElapse')*7

        estimate = {
            "impact": {
                'currentlyInfected': data.get('reportedCases') * 10,
                'infectionsByResquestedTime': estimate.get('impact').get('currentlyInfected') * 137,
                'severeCasesByRequestedTime': estimate.get('impact').get('infectionByRequestedTime') * 0.15,
                'hospitalBedsByRequestedTime': data.get('totalHospitalBeds')*0.35 - estimate.get('impact').get(
                    'severeCasesByRequestedTime'),
                'casesForICUByRequestedTime': estimate.get('impact').get('infectionsByRequestedTime') * 0.05,
                'casesForVentilatorsByRequestedTime': estimate.get('impact').get('infectionsByRequestedTime') * 0.02,
                'dollarsInFlight': math.trunc((estimate.get('infectionsByRequestedTime')
                                               * data.get('region').get('avgDailyIncomePopulation')
                                               * data.get('region').get) / periodTime)

            },
            "severeImpact": {
                'currentlyInfected': data.get('reportedCases') * 50,
                'infectionsByResquetedTime': estimate.get('severeImpact').get('currentlyInfected') * 137,
                'severeCasesByRequestedTime': estimate.get('severeImpact').get('infectionByRequestedTime') * 0.15,
                'hospitalBedsByRequestedTime': data.get('totalHospitalBeds')*0.35 - estimate.get('severeImpact').get(
                    'severeCasesByRequestedTime'),
                'casesForICUByRequestedTime': estimate.get('severeImpact').get('infectionsByRequestedTime') * 0.05,
                'casesForVentilatorsByRequestedTime': estimate.get('severeImpact').get('infectionsByRequestedTime') * 0.02,
                'dollarsInFlight': math.trunc((estimate.get('infectionsByRequestedTime')
                                               * data.get('region').get('avgDailyIncomePopulation')
                                               * data.get('region').get) / periodTime)
            }
        }

    elif data['periodeType'] == 'months':
        periodTime = data.get('timeToElapse') * 30

        estimate = {
            "impact": {
                'currentlyInfected': data.get('reportedCases') * 10,
                'infectionsByRequestedTime': estimate.get('impact').get('currentlyInfected') * 548,
                'severeCasesByRequestedTime': estimate.get('impact').get('infectionByRequestedTime') * 0.15,
                'hospitalBedsByRequestedTime': data.get('totalHospitalBeds')*0.35 - estimate.get('impact').get(
                    'severeCasesByRequestedTime'),
                'casesForICUByRequestedTime': estimate.get('impact').get('infectionsByRequestedTime') * 0.05,
                'casesForVentilatorsByRequestedTime': estimate.get('impact').get('infectionsByRequestedTime') * 0.02,
                'dollarsInFlight': math.trunc((estimate.get('infectionsByRequestedTime')
                                               * data.get('region').get('avgDailyIncomePopulation')
                                               * data.get('region').get) / periodTime)
            },
            "severeImpact": {
                'currentlyInfected': data['reportedCases'] * 50,
                'infectionsByResquetedTime': estimate.get('severeImpact').get('currentlyInfected') * 548,
                'severeCasesByRequestedTime': estimate.get('severeImpact').get('infectionByRequestedTime') * 0.15,
                'hospitalBedsByRequestedTime': data.get('totalHospitalBeds')*0.35 - estimate.get('severeImpact').get(
                    'severeCasesByRequestedTime'),
                'casesForICUByRequestedTime': estimate.get('severeImpact').get('infectionsByRequestedTime') * 0.05,
                'casesForVentilatorsByRequestedTime': estimate.get('severeImpact').get('infectionsByRequestedTime') * 0.02,
                'dollarsInFlight': math.trunc((estimate.get('infectionsByRequestedTime')
                                               * data.get('region').get('avgDailyIncomePopulation')
                                               * data.get('region').get) / periodTime)
            }
        }

    else:
        print("Choose the valid periode Type.")

    return { data:{}, estimate['impact']:{}, estimate['severeImpact']:{}}


  




