#This is your class for cards
class Card:
  def __init__(self, name, level,maxLevel,count):
    self.name = name
    self.level = level
    self.maxLevel = maxLevel
    self.count = count

  def __str__(self):
    # note maxLevel is not needed to be displayed. this is only needed for the upgrade of one level for one type of card.
    return f"{self.name} (Level: {self.level}, Count: {self.count})"

headers = {
    "Accept": "application/json",
    "authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImFmNDk2M2NlLTU3NjctNGYyYi1hNDYzLWEwOGM5OGYxNjZkYSIsImlhdCI6MTY3OTIyNDkyOSwic3ViIjoiZGV2ZWxvcGVyL2YxYzQ1ZTg1LTc4NjQtOGJjYi00OWE4LTNjZGU4YzJhYjYxNiIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyIxODguMjEzLjEzOC4yMTYiXSwidHlwZSI6ImNsaWVudCJ9XX0.70WZgFaB9Rix56YxoKzh-BHJOBbu_V3s3imUxxD6wSay5kWZMkmNL3Xn82HVPHXxTa_oXNbLtdZMFY1CV-Z02g"

}


