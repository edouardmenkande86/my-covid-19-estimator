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
        'impact':{
            'currentlyInfected':data['reportedCases'] * 10
        },
        'severeImpact': {
            'currentlyInfected': data['reportedCases'] * 50
        }
    }
    if data['periodeType'] == 'days':
        estimate = {
            'impact': {
                'currentlyInfected': data['reportedCases'] * 10,
                'infectionsByRequestedTime': estimate['impact']['currentlyInfected'] * 18
            },
            'severeImpact': {
                'currentlyInfected': data['reportedCases'] * 50,
                'infectionsByRequestedTime': estimate['severeImpact']['currentlyInfected'] * 18
            }

        }
    elif data['periodeType'] == 'weeks':
        estimate = {
            'impact': {
                'currentlyInfected': data['reportedCases'] * 10,
                'infectionsByResquestedTime': estimate['impact']['currentlyInfected'] * 137
            },
            'severeImpact': {
                'currentlyInfected': data['reportedCases'] * 50,
                'infectionsByResquetedTime': estimate['severeImpact']['currentlyInfected'] * 137
            }
        }

    elif data['periodeType'] == 'months':
        estimate = {
            'impact': {
                'currentlyInfected': data['reportedCases'] * 10,
                'infectionsByRequestedTime': estimate['impact']['currentlyInfected'] * 548
            },
            'severeImpact': {
                'currentlyInfected': data['reportedCases'] * 50,
                'infectionsByResquetedTime': estimate['severeImpact']['currentlyInfected'] * 548
            }
        }

    else:
        print("Choose the valid periode Type.")



    return data

  




