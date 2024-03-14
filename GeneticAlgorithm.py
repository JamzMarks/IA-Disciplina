import yaml;
import random;

class Config (object):
    _instance = None
    def __init__(self):
        with open("ga_config.yaml") as stream:
            try:
                yamlConfig = yaml.safe_load(stream);
                self.mutationRate = yamlConfig["mutationRate"];
                self.populationSize = yamlConfig["populationSize"];
                self.maxGeneration = yamlConfig["maxGeneration"];
                self.selectionRate = yamlConfig["selectionRate"];
            except yaml.YAMLError as exc:
                print(exc);

    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

class Individual (object):
    def __init__(self,
                 chromosomeSize:int):
        self.config = Config();
        self.chromosomeSize = chromosomeSize;
        self.chromosome = [];
        self.targetFunction = 0;
        self.mutationRate = self.config.mutationRate;

    def createChromosome (self,
                          target:str=None,
                          father:list=[],
                          mother:list=[]):
        if not(target is None):
            self.chromosome = [ord(char) for char in target];
        elif ((len(father)) != 0 and (len(mother) != 0)):
            self.chromosome = father + mother;
        else:
            for i in range(0, self.chromosomeSize, 1):
                self.chromosome.append(random.randint(0,255));

    def calculateTargetFunction(self,
                                target:object):
        for i in range(0, len(target.chromosome),1):
            if self.chromosome[i] == target.chromosome[i]:
                self.targetFunction += 1;
    
    def resetTargetFunction(self):
        self.targetFunction = 0;

    def mutate(self):
        self.chromosome[random.randint(0,len(self.chromosome) - 1)] = random.randint(0,255);

    def getWord(self) -> str:
        return ''.join(chr(gene) for gene in self.chromosome)

def main():
    individual = Individual(4);
    individual.createChromosome();
    print(individual.chromosome)
    print(individual.getWord());

if __name__ == "__main__":
    main();
