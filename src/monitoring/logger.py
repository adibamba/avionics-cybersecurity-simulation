import logging

def setup_logger(name, log_file, level=logging.INFO):
    handler = logging.FileHandler(log_file)
    handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)
    
    return logger

simulation_logger = setup_logger('simulation_logger', 'simulation.log')
attack_logger = setup_logger('attack_logger', 'attack.log')
defense_logger = setup_logger('defense_logger', 'defense.log')