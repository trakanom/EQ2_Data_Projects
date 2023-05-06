from abc import ABC, abstractmethod

    '''
    - Deals X damage to target
    - Deals Y damage to target
    - Deals Z damage to target instantly and every T seconds
        - On termination, applies A.
            - Deals x damage to target
    '''

    '''
    - Applies Death Mark when Activate:
        - on TakeMeleeDamage this spell has a 5% chance to cast Marked
            - 
    
    '''



class Ability(ABC):
    "Ability_Name",
    "Ability_Type", # Attack, Heal, Buff, Rez, 
    "Target_Type", # Single (red) (default), Enc_AOE (green), PB_AOE (blue), T_AOE (Blue), Self (Yellow), Group (Purple), Raid (Purple)
    "Cast_Time", # 
    "Reuse_Time",
    "Recovery_Time", # 0.5 (default)    



class Attack(Ability):
    "Damage_Min"
    "Damage_Max"
    
class AoE(Attack):
    "Max_Targets", # 1 (default), 0 for unlimited (rare cases), 8 for most blue

    
    

    
class DoT(Attack):
    "Dmg_Init_Min",
    "Dmg_Init_Max",
    "Dmg_Tick_Min",
    "Dmg_Tick_Max",
    "Tick_Rate",