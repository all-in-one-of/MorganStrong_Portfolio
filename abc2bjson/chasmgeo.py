"""
File:       chasmgeo.py
Author:     Morgan Strong, Elizabeth Brayton
Date:       11/26/12. Modified: 7/26/2013
Project:    BYU Senior Animation: Chasm

Description:
    Project specific definitions for the 2013 BYU Animated short: Chasm.
    This code was located elsewhere during the actual project but has been
    included here for completeness and simplicity.

"""

from abc2bjson_hou import prependNamespace

################################################################################
#
# DATA
#
################################################################################

_objectName = ""
_objects = {
            'Wheel': 'wheel',
            'Welding Mask': 'mask',
            'Wings':'wings',
            'Jacket': 'jacket',
            'Addison': 'addison',
            'Picture Frame': 'frame',
            'Workshop Shelf': 'shelf',
            'Wooden Stool': 'stool'
           }


################################################################################
#
# GEOMETRY DICTIONARIES
#
################################################################################

def getFrameGeoDict():
    BackShade = ['Picture_Frame/Backing']
    FrameBody = ['Picture_Frame/Main']
    PicturelayerNew = ['Picture_Frame/Photo']
    FrameGlass1 = ['Picture_Frame/Glass']
    BrokenGlass = ['Picture_Frame/Glass_Broken']
    doodads = ['Picture_Frame/Clasps']

    pcs = {'back':BackShade,\
           'main':FrameBody,\
           'photo':PicturelayerNew,\
           'glass':FrameGlass1,\
           'glass_broken':BrokenGlass,\
           'clasps':doodads}

    # Prepend the namespace to each level of the geoemtry path hard coded above.
    pcs = prependNamespace(pcs)
    return pcs

def getShelfGeoDict():
    shelf = ['polySurface1']

    pcs = {'shelf':shelf}

    # Prepend the namespace to each level of the geoemtry path hard coded above.
    pcs = prependNamespace(pcs)
    return pcs

def getStoolGeoDict():
    wood = ['polySurface1']
    
    pcs = {'stool':wood}

    # Prepend the namespace to each level of the geoemtry path hard coded above.
    pcs = prependNamespace(pcs)
    return pcs

def getWheelGeoDict():
    chasm_uber_RUST_RING = ['wheel/wheel_Back_Plate']
    chasm_uber_rust_COPPER = ['wheel/wheel_Base']
    uber_SteelNoREFL = ['wheel/wheel_base_bolts_bottom',\
          'wheel/wheel_spoke_bolts']
    chasm_rust_DULL1 = ['wheel/wheel_base_bolts_top',\
            'wheel/wheel_base_pipeConnectors']
    uber_ShinySteel = ['wheel/wheel_base_coils',\
            'wheel/wheel_spoke_baseA',\
            'wheel/wheel_spoke_baseB']
    rust_squarePipeBases = ['wheel/wheel_base_connectors']
    uber_Copper1 = ['wheel/wheel_base_pipes']
    uber_Wraps = ['wheel/wheel_spoke_wrappings']
    uber_Handles = ['wheel/wheel_spoke_handles']
    uber_Copper = ['wheel/wheel_spoke_rivets']
    uber_LightNoREFL = ['wheel/wheel_spoke_sockets']
    uber_CopperWires = ['wheel/wheel_spoke_tubes']

    pcs ={'back_plate':chasm_uber_RUST_RING,\
          'base':chasm_uber_rust_COPPER,\
          'bolts_steel':uber_SteelNoREFL,\
          'bolts_dull':chasm_rust_DULL1,\
          'coils_spoke_base':uber_ShinySteel,\
          'base_conn':rust_squarePipeBases,\
          'base_pipes':uber_Copper1,\
          'wraps':uber_Wraps,\
          'handles':uber_Handles,\
          'rivets':uber_Copper,\
          'sockets':uber_LightNoREFL,\
          'tubes':uber_CopperWires}

    # Prepend the namespace to each level of the geoemtry path hard coded above.
    pcs = prependNamespace(pcs)
    return pcs

def getWeldingMaskGeoDict():
    # Hard Coded Pieces of weldingMask
    straps = ['weldingMask/strap']
    sens = ['weldingMask/mask/sensor']
    mtl1 = ['weldingMask/mask']
    mtl2 = ['weldingMask/mask/glassFrame',\
                'weldingMask/knob_L',\
                'weldingMask/knob_R']
    glass = ['weldingMask/mask/glass']

    pcs ={'straps':straps,\
          'sensor':sens,\
          'mask':mtl1,\
          'knobs_and_frame':mtl2,\
          'glass':glass}

    # Prepend the namespace to each level of the geoemtry path hard coded above.
    pcs = prependNamespace(pcs)
    return pcs

def getWingGeoDict():
    cntr = ['model01/FeatherGeo/y']
    fthrs = ['model01/FeatherGeo/R_Feathers', \
             'model01/FeatherGeo/L_Feathers']

    hns = ['model01/Gp_Wings/Gp_R_Wing/R_StrapLow',\
           'model01/Gp_Wings/Gp_R_Wing/R_StrapHigh',\
           'model01/Gp_Wings/Gp_L_Wing/L_StrapLow',\
           'model01/Gp_Wings/Gp_L_Wing/L_StrapHigh']
    mtl = ['model01/Gp_Wings/Gp_L_Wing/L_Humerus1',\
           'model01/Gp_Wings/Gp_L_Wing/L_Humerus2',\
           'model01/Gp_Wings/Gp_L_Wing/L_WristPivot',\
           'model01/Gp_Wings/Gp_L_Wing/L_ElbowPivot1',\
           'model01/Gp_Wings/Gp_L_Wing/L_ElbowPivot2',\
           'model01/Gp_Wings/Gp_L_Wing/L_HandlePivot',\
           'model01/Gp_Wings/Gp_L_Wing/L_Handle',\
           'model01/Gp_Wings/Gp_L_Wing/Gp_L_Index',\
           'model01/Gp_Wings/Gp_L_Wing/Gp_L_Middle',\
           'model01/Gp_Wings/Gp_L_Wing/Gp_L_Ring',\
           'model01/Gp_Wings/Gp_L_Wing/Gp_L_Pinky',\
           'model01/Gp_Wings/Gp_L_Wing/L_Spring',\
           'model01/Gp_Wings/Gp_L_Wing/Gp_L_Forewing',\
           'model01/Gp_Wings/Gp_L_Wing/L_SpringCatchLow',\
           'model01/Gp_Wings/Gp_L_Wing/L_EndCableAnchor',\
           'model01/Gp_Wings/Gp_L_Wing/L_MedialCableAnchor',\
           'model01/Gp_Wings/Gp_L_Wing/R_SpringHookLow',\
           'model01/Gp_Wings/Gp_L_Wing/R_SpringHookHigh',\
           'model01/Gp_Wings/Gp_R_Wing/R_Humerus1',\
           'model01/Gp_Wings/Gp_R_Wing/R_Humerus2',\
           'model01/Gp_Wings/Gp_R_Wing/R_WristPivot',\
           'model01/Gp_Wings/Gp_R_Wing/R_ElbowPivot1',\
           'model01/Gp_Wings/Gp_R_Wing/R_ElbowPivot2',\
           'model01/Gp_Wings/Gp_R_Wing/R_HandlePivot',\
           'model01/Gp_Wings/Gp_R_Wing/R_Handle',\
           'model01/Gp_Wings/Gp_R_Wing/Gp_R_Index',\
           'model01/Gp_Wings/Gp_R_Wing/Gp_R_Middle',\
           'model01/Gp_Wings/Gp_R_Wing/Gp_R_Ring',\
           'model01/Gp_Wings/Gp_R_Wing/Gp_R_Pinky',\
           'model01/Gp_Wings/Gp_R_Wing/R_Spring',\
           'model01/Gp_Wings/Gp_R_Wing/Gp_R_Forewing',\
           'model01/Gp_Wings/Gp_R_Wing/R_SpringCatchLow',\
           'model01/Gp_Wings/Gp_R_Wing/R_EndCableAnchor',\
           'model01/Gp_Wings/Gp_R_Wing/R_MedialCableAnchor',\
           'model01/Gp_Wings/Gp_R_Wing/R_SpringHookLow',\
           'model01/Gp_Wings/Gp_R_Wing/R_SpringHookHigh']
    rub = ['model01/Gp_Wings/BackStrap',\
           'model01/Gp_Wings/Gp_R_Wing/R_RubberShoulder1',\
           'model01/Gp_Wings/Gp_R_Wing/R_RubberShoulder2',\
           'model01/Gp_Wings/Gp_L_Wing/L_RubberShoulder1',\
           'model01/Gp_Wings/Gp_L_Wing/L_RubberShoulder2']
    pads = ['model01/Gp_Wings/Gp_R_Wing/R_Scap',\
            'model01/Gp_Wings/Gp_L_Wing/L_Scap']
    wrs = ['model01/Gp_Wings/Gp_L_Wing/L_DriveCable2',\
           'model01/Gp_Wings/Gp_L_Wing/L_DriveCable1',\
           'model01/Gp_Wings/Gp_L_Wing/Gp_Cables',\
           'model01/Gp_Wings/Gp_R_Wing/R_DriveCable2',\
           'model01/Gp_Wings/Gp_R_Wing/R_DriveCable1',\
           'model01/Gp_Wings/Gp_R_Wing/Gp_Cables']
    # TODO: mechanical part
    pcs = {'center':cntr,\
           'primaries':fthrs,\
           'harness':hns,\
           'metal':mtl,\
           'rubber':rub,\
           'pads':pads,\
           'wires':wrs}

    # Prepend the namespace to each level of the geoemtry path hard coded above.
    pcs = prependNamespace(pcs)
    return pcs

def getJacketGeoDict():
    main = ['model01/grp_Jacket_01/jacketMain_01']
    elbow = ['model01/grp_Jacket_01/JacketElbowPads_01']
    patch = ['model01/grp_Jacket_01/jacketPatch_01']
    wingP = ['model01/grp_Jacket_01/jacketInsideLining_01']

    pcs = {'main':main,\
           'elbow':elbow,\
           'patch':patch,\
           'wing_patch':wingP}
    # Prepend the namespace to each level of the geoemtry path hard coded above.
    pcs = prependNamespace(pcs)
    return pcs

def getAddisonGeoDict():
    # Hard Coded Pieces of Addison
    eI  = ['model01/grp_L_eye_01/eye_L_Inner_01',\
           'model01/grp_R_eye_01/eye_R_Inner_01']
    eO  = ['model01/grp_L_eye_01/eye_L_Outer_01',\
           'model01/grp_R_eye_01/eye_R_Outer_01']
    eB  = ['model01/grp_L_eye_01/eye_L__Back_01',\
           'model01/grp_R_eye_01/eye_R__Back_01']
    tth = ['model01/lower_teeth',\
           'model01/upper_teeth']
    mth = ['model01/mouthAndTeeth/mouth_Interiorwalls']
    hd  = ['/model01/head']
    mtl = ['/model01/lower_body/grp_Boot_L/eyelets_L',\
           '/model01/lower_body/grp_Boot_L/buckle_top_L',\
           '/model01/lower_body/grp_Boot_L/buckle_bottom_L',\
           '/model01/lower_body/grp_Boot_R/eyelets_R',\
           '/model01/lower_body/grp_Boot_R/buckle_top_R',\
           '/model01/lower_body/grp_Boot_R/buckle_bottom_R',\
           '/model01/upper_body/grp_Vest/hairSystem5Follicles',\
           '/model01/upper_body/grp_Vest/hairSystem4Follicles',\
           '/model01/upper_body/grp_Vest/hairSystem3Follicles',\
           '/model01/upper_body/grp_Vest/hairSystem2Follicles',\
           '/model01/upper_body/grp_Vest/hairSystem1Follicles',\
           '/model01/upper_body/grp_Vest/vestBuckle_L',\
           '/model01/upper_body/grp_Vest/vestBuckle_R']
    btLcs=['/model01/lower_body/grp_Boot_L/laces_L',\
           '/model01/lower_body/grp_Boot_R/laces_R']
    btns = ['/model01/upper_body/grp_Shirt/polySurface9/polySurface1',\
            '/model01/upper_body/grp_Shirt/polySurface10/polySurface4',\
            '/model01/upper_body/grp_Shirt/polySurface11/polySurface7',\
            '/model01/upper_body/grp_Shirt/polySurface12/polySurface10']
    shrt= ['/model01/upper_body/grp_Shirt/polySurface4',\
           '/model01/upper_body/grp_Shirt/pCube1',\
           '/model01/upper_body/grp_Shirt/pCube2',\
           '/model01/upper_body/grp_Shirt/polySurface11/polySurface8',\
           '/model01/upper_body/grp_Shirt/polySurface11/polySurface9',\
           '/model01/upper_body/grp_Shirt/polySurface9/polySurface2',\
           '/model01/upper_body/grp_Shirt/polySurface9/polySurface3',\
           '/model01/upper_body/grp_Shirt/polySurface10/polySurface5',\
           '/model01/upper_body/grp_Shirt/polySurface10/polySurface6',\
           '/model01/upper_body/grp_Shirt/polySurface12/polySurface11',\
           '/model01/upper_body/grp_Shirt/polySurface12/polySurface12']
    vst = ['/model01/upper_body/grp_Vest/vest',\
           '/model01/upper_body/grp_Vest/vestStrap_L',\
           '/model01/upper_body/grp_Vest/vestStrap_R']
    pnts= ['/model01/lower_body/grp_Pants']
    arms= ['/model01/upper_body/arm_L',\
           '/model01/upper_body/arm_R']
    btM = ['/model01/lower_body/grp_Boot_L/boot_L',\
           '/model01/lower_body/grp_Boot_L/belt_top_L',\
           '/model01/lower_body/grp_Boot_L/belt_bottom_L',\
           '/model01/lower_body/grp_Boot_R/boot_R',\
           '/model01/lower_body/grp_Boot_R/belt_top_R',\
           '/model01/lower_body/grp_Boot_R/belt_bottom_R']
    btS = ['/model01/lower_body/grp_Boot_L/tread_L',\
           '/model01/lower_body/grp_Boot_R/tread_R']

    pcs ={'eyes_inner':eI,\
          'eyes_outer':eO,\
          'eyes_back':eB,\
          'teeth':tth,\
          'mouth_inner':mth,\
          'head':hd,\
          'metal':mtl,\
          'bootLaces':btLcs,\
          'buttons':btns,\
          'shirt':shrt,\
          'vest':vst,\
          'pants':pnts,\
          'arms':arms,\
          'bootsMain':btM,\
          'bootSoles':btS}
    
    # Prepend the namespace to each level of the geoemtry path hard coded above.
    pcs = prependNamespace(pcs)
    return pcs

def getGeoDict():
    result = {}
    if _objectName == _objects["Wheel"]:
        result = getWheelGeoDict()
    elif _objectName == _objects["Welding Mask"]:
        result = getWeldingMaskGeoDict()
    elif _objectName == _objects["Wings"]:
        result = getWingGeoDict()
    elif _objectName == _objects["Jacket"]:
        result = getJacketGeoDict()
    elif _objectName == _objects["Addison"]:
        result = getAddisonGeoDict()
    elif _objectName == _objects["Picture Frame"]:
        result = getFrameGeoDict()
    elif _objectName == _objects["Wooden Stool"]:
        result = getStoolGeoDict()
    elif _objectName == _objects["Workshop Shelf"]:
        result = getShelfGeoDict()
    return result


################################################################################
#
# SHOT LIST / LOCATIONS
#
################################################################################

def getChasmShotList():
    A = ["A"+str(n).zfill(2) for n in range(1,12)]
    B = ["B"+str(n).zfill(2) for n in range(1,16)]
    C = ["C"+str(n).zfill(2) for n in range(1,13)]
    D = ["D"+str(n).zfill(2) for n in range(1,18)]
    E = ["E"+str(n).zfill(2) for n in range(1,6)]
    return A+B+C+D+E

def _interpretChoice(shot_num):
	# Converts shot name to a directory path for our output
    #print (_objectName)
    path = os.path.join("$JOB/CHASM_PROJECT/sequences/",\
                        shot_num[0],\
                        str(shot_num[1:]),\
                        "Animation_" + shot_num,\
                        _objectName + "_bjson") + os.sep
    return path


################################################################################
#
# HOUDINI DIALOGS
#
################################################################################

def getObjectToImport():
    """
    Return the user-specified, predefined object they will be exporting from the
    Alembic file.
    """
    choices = _objects.keys()
    c = hou.ui.selectFromList(choices,\
                               exclusive = True,\
                               title = 'Choose the object you are trying to import',\
                               num_visible_rows = len(choices))
    if not c:
        raise Exception("Nothing Selected. Exiting...")
    
    global _objectName
    _objectName = _objects.get(choices[c[0]])
