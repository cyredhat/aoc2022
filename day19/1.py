from collections import namedtuple
from functools import cache

# data = open('day19/tc.txt').read()
data = open('day19/input.txt').read()

Blueprint = namedtuple('Blueprint', "oreCost clayCost obsidianCost geodeCost")

bps = []
for line in data.split('\n'):
  blueprint = []
  for word in line.split(' '):
    try:
      blueprint.append(int(word))
    except:
      pass
  blueprint = Blueprint(blueprint[0], blueprint[1], (blueprint[2], blueprint[3]), (blueprint[4], blueprint[5]))
  bps.append(blueprint)

@cache
def maxGeodePossible(timeLeft):
  return maxGeodePossible(timeLeft - 1) + timeLeft if timeLeft > 0 else 0

State = namedtuple('State', "time ore clay obsidian oreBot clayBot obsidianBot geodeBot")
memo = {}
timeLimit = 24
def solve(state: State, blueprint: Blueprint, geodeCount: int) -> None:
  global maxGeodeCount, timeLimit
  maxGeodeCount = max(maxGeodeCount, geodeCount)
  time, ore, clay, obsidian, oreBot, clayBot, obsidianBot, geodeBot = state
  maxOreSpend = max(blueprint.oreCost, blueprint.clayCost, blueprint.obsidianCost[0], blueprint.geodeCost[0])
  maxClaySpend = blueprint.obsidianCost[1]
  maxObsidianSpend = blueprint.geodeCost[1]
  if time > timeLimit:
    return
  if geodeCount + maxGeodePossible(timeLimit - time) <= maxGeodeCount:
    return
  if (state, blueprint) in memo and memo[(state, blueprint)] >= geodeCount:
    return
  memo[(state, blueprint)] = geodeCount
  oreOld, clayOld, obsidianOld = ore, clay, obsidian
  ore += oreBot
  clay += clayBot
  obsidian += obsidianBot

  if oreOld >= blueprint.oreCost and oreBot < maxOreSpend:
    solve(State(time + 1, ore - blueprint.oreCost, clay, obsidian, oreBot + 1, clayBot, obsidianBot, geodeBot), blueprint, geodeCount)
  if oreOld >= blueprint.clayCost and clayBot < maxClaySpend:
    solve(State(time + 1, ore - blueprint.clayCost, clay, obsidian, oreBot, clayBot + 1, obsidianBot, geodeBot), blueprint, geodeCount)
  if oreOld >= blueprint.obsidianCost[0] and clayOld >= blueprint.obsidianCost[1] and obsidianBot < maxObsidianSpend:
    solve(State(time + 1, ore - blueprint.obsidianCost[0], clay - blueprint.obsidianCost[1], obsidian, oreBot, clayBot, obsidianBot + 1, geodeBot), blueprint, geodeCount)
  if oreOld >= blueprint.geodeCost[0] and obsidianOld >= blueprint.geodeCost[1]:
    solve(State(time + 1, ore - blueprint.geodeCost[0], clay, obsidian - blueprint.geodeCost[1], oreBot, clayBot, obsidianBot, geodeBot + 1), blueprint, geodeCount + (timeLimit - time))
    return
  solve(State(time + 1, ore, clay, obsidian, oreBot, clayBot, obsidianBot, geodeBot), blueprint, geodeCount)

initialState = State(1, 0, 0, 0, 1, 0, 0, 0)
quality = 0
for i, blueprint in enumerate(bps):
  print(blueprint)
  maxGeodeCount = 0
  maxGeodes = [0] * (timeLimit + 1)
  solve(initialState, blueprint, 0)
  print(i+1, maxGeodeCount)
  quality += maxGeodeCount * (i + 1)

print(quality)
