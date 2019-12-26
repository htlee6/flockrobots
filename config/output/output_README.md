# Output

Here we use a JSON file to restore the default settings on the output configuration. 

The basic structure is as followed. 

1. OutputDirectory
    
    Type: `String` \
    The relative directory of the output file, relative to `main.py`. 

2. OutputFilename

    Type: `String`\
    The filename of the output file. 
    P.S. Name Only, No Extension Needed!
    
3. ifSaveDetail
    
    Type: `String`\
    To decide if to save some detailed information. 

    | Type | Content | Description|
    |------|---------|:------------:|
    | `String` | `true` | Switch on the option, aka save |
    | `String` | `false` | Switch off the option, aka not save |
    | `String` | `stat` | Not clear yet |
    
    1. SaveDistanceBetweenUnits: 
    If save distance between units.
       
    2. SaveDistanceBetweenNeighbours: 
    If save distance between neighbours. 
        
    3. SaveVelocity: 
    If save velocity of units.
        
    4. SaveCorrelation: 
    If save correlation. 
    
    5. SaveCoM: 
    If save CoM, aka `Center of Mass`. 
    
    6. SaveCollisions: 
    If save collisions between units. 
    
    7. SaveCollisionRatio:
    If save ratio of collision. 
    
    8. SaveAcceleration: 
    If save the acceleration of units. 