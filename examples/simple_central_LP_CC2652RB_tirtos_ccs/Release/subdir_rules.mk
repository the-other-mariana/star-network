################################################################################
# Automatically-generated file. Do not edit!
################################################################################

SHELL = cmd.exe

# Each subdirectory must supply rules for building sources it contributes
build-1587915215: ../simple_central.syscfg
	@echo 'Building file: "$<"'
	@echo 'Invoking: SysConfig'
	"C:/ti/sysconfig_1.10.0/sysconfig_cli.bat" -s "C:/ti/simplelink_cc13xx_cc26xx_sdk_5_40_00_40/.metadata/product.json" --script "C:/Users/mariana/workspace_v11/simple_central_LP_CC2652RB_tirtos_ccs/simple_central.syscfg" -o "syscfg" --compiler ccs
	@echo 'Finished building: "$<"'
	@echo ' '

syscfg/ti_ble_config.h: build-1587915215 ../simple_central.syscfg
syscfg/ti_ble_config.c: build-1587915215
syscfg/ti_build_config.opt: build-1587915215
syscfg/ti_ble_app_config.opt: build-1587915215
syscfg/ti_devices_config.c: build-1587915215
syscfg/ti_radio_config.c: build-1587915215
syscfg/ti_radio_config.h: build-1587915215
syscfg/ti_drivers_config.c: build-1587915215
syscfg/ti_drivers_config.h: build-1587915215
syscfg/ti_utils_build_linker.cmd.genlibs: build-1587915215
syscfg/syscfg_c.rov.xs: build-1587915215
syscfg/ti_utils_runtime_model.gv: build-1587915215
syscfg/ti_utils_runtime_Makefile: build-1587915215
syscfg/: build-1587915215

syscfg/%.obj: ./syscfg/%.c $(GEN_OPTS) | $(GEN_FILES) $(GEN_MISC_FILES)
	@echo 'Building file: "$<"'
	@echo 'Invoking: Arm Compiler'
	"C:/ti/ccs1110/ccs/tools/compiler/ti-cgt-arm_20.2.5.LTS/bin/armcl" --cmd_file="C:/Users/mariana/workspace_v11/simple_central_LP_CC2652RB_tirtos_ccs/Release/syscfg/ti_ble_app_config.opt" --cmd_file="C:/Users/mariana/workspace_v11/simple_central_LP_CC2652RB_tirtos_ccs/Release/syscfg/ti_build_config.opt" --cmd_file="C:/ti/simplelink_cc13xx_cc26xx_sdk_5_40_00_40/source/ti/ble5stack/config/build_components.opt" --cmd_file="C:/ti/simplelink_cc13xx_cc26xx_sdk_5_40_00_40/source/ti/ble5stack/config/factory_config.opt"  -mv7M4 --code_state=16 --float_support=FPv4SPD16 -me -O4 --opt_for_speed=0 --include_path="C:/Users/mariana/workspace_v11/simple_central_LP_CC2652RB_tirtos_ccs" --include_path="C:/Users/mariana/workspace_v11/simple_central_LP_CC2652RB_tirtos_ccs/Release" --include_path="C:/Users/mariana/workspace_v11/simple_central_LP_CC2652RB_tirtos_ccs/Application" --include_path="C:/ti/simplelink_cc13xx_cc26xx_sdk_5_40_00_40/source" --include_path="C:/ti/simplelink_cc13xx_cc26xx_sdk_5_40_00_40/source/ti" --include_path="C:/ti/simplelink_cc13xx_cc26xx_sdk_5_40_00_40/source/ti/ble5stack" --include_path="C:/ti/simplelink_cc13xx_cc26xx_sdk_5_40_00_40/source/ti/ble5stack/controller/cc26xx/inc" --include_path="C:/ti/simplelink_cc13xx_cc26xx_sdk_5_40_00_40/source/ti/ble5stack/inc" --include_path="C:/ti/simplelink_cc13xx_cc26xx_sdk_5_40_00_40/source/ti/ble5stack/rom" --include_path="C:/ti/simplelink_cc13xx_cc26xx_sdk_5_40_00_40/source/ti/ble5stack/common/cc26xx" --include_path="C:/ti/simplelink_cc13xx_cc26xx_sdk_5_40_00_40/source/ti/ble5stack/icall/inc" --include_path="C:/ti/simplelink_cc13xx_cc26xx_sdk_5_40_00_40/source/ti/ble5stack/hal/src/target/_common" --include_path="C:/ti/simplelink_cc13xx_cc26xx_sdk_5_40_00_40/source/ti/ble5stack/hal/src/target/_common/cc26xx" --include_path="C:/ti/simplelink_cc13xx_cc26xx_sdk_5_40_00_40/source/ti/ble5stack/hal/src/inc" --include_path="C:/ti/simplelink_cc13xx_cc26xx_sdk_5_40_00_40/source/ti/ble5stack/heapmgr" --include_path="C:/ti/simplelink_cc13xx_cc26xx_sdk_5_40_00_40/source/ti/ble5stack/profiles/dev_info" --include_path="C:/ti/simplelink_cc13xx_cc26xx_sdk_5_40_00_40/source/ti/ble5stack/profiles/simple_profile" --include_path="C:/ti/simplelink_cc13xx_cc26xx_sdk_5_40_00_40/source/ti/ble5stack/icall/src/inc" --include_path="C:/ti/simplelink_cc13xx_cc26xx_sdk_5_40_00_40/source/ti/ble5stack/osal/src/inc" --include_path="C:/ti/simplelink_cc13xx_cc26xx_sdk_5_40_00_40/source/ti/ble5stack/services/src/saddr" --include_path="C:/ti/simplelink_cc13xx_cc26xx_sdk_5_40_00_40/source/ti/ble5stack/services/src/sdata" --include_path="C:/ti/simplelink_cc13xx_cc26xx_sdk_5_40_00_40/source/ti/common/nv" --include_path="C:/ti/simplelink_cc13xx_cc26xx_sdk_5_40_00_40/source/ti/common/cc26xx" --include_path="C:/ti/simplelink_cc13xx_cc26xx_sdk_5_40_00_40/kernel/tirtos/packages" --include_path="C:/ti/simplelink_cc13xx_cc26xx_sdk_5_40_00_40/source/ti/devices/cc13x2_cc26x2" --include_path="C:/ti/simplelink_cc13xx_cc26xx_sdk_5_40_00_40/source/ti/posix/ccs" --include_path="C:/ti/ccs1110/ccs/tools/compiler/ti-cgt-arm_20.2.5.LTS/include" --define=DeviceFamily_CC26X2 --define=FLASH_ROM_BUILD --define=NVOCMP_NWSAMEITEM=1 -g --c99 --gcc --diag_warning=225 --diag_warning=255 --diag_wrap=off --display_error_number --gen_func_subsections=on --abi=eabi --preproc_with_compile --preproc_dependency="syscfg/$(basename $(<F)).d_raw" --include_path="C:/Users/mariana/workspace_v11/simple_central_LP_CC2652RB_tirtos_ccs/Release/syscfg" --obj_directory="syscfg" $(GEN_OPTS__FLAG) "$<"
	@echo 'Finished building: "$<"'
	@echo ' '

build-1950957153:
	@$(MAKE) --no-print-directory -Onone -f subdir_rules.mk build-1950957153-inproc

build-1950957153-inproc: ../simple_central_app.cfg
	@echo 'Building file: "$<"'
	@echo 'Invoking: XDCtools'
	"C:/ti/ccs1110/xdctools_3_62_01_16_core/xs" --xdcpath="C:/ti/simplelink_cc13xx_cc26xx_sdk_5_40_00_40/source;C:/ti/simplelink_cc13xx_cc26xx_sdk_5_40_00_40/kernel/tirtos/packages;" xdc.tools.configuro -o configPkg -t ti.targets.arm.elf.M4F -p ti.platforms.simplelink:CC2652RB1F -r release -c "C:/ti/ccs1110/ccs/tools/compiler/ti-cgt-arm_20.2.5.LTS" --compileOptions "-mv7M4 --code_state=16 --float_support=FPv4SPD16 -me -O4 --opt_for_speed=0 --include_path=\"C:/Users/mariana/workspace_v11/simple_central_LP_CC2652RB_tirtos_ccs\" --include_path=\"C:/Users/mariana/workspace_v11/simple_central_LP_CC2652RB_tirtos_ccs/Release\" --include_path=\"C:/Users/mariana/workspace_v11/simple_central_LP_CC2652RB_tirtos_ccs/Application\" --include_path=\"C:/ti/simplelink_cc13xx_cc26xx_sdk_5_40_00_40/source\" --include_path=\"C:/ti/simplelink_cc13xx_cc26xx_sdk_5_40_00_40/source/ti\" --include_path=\"C:/ti/simplelink_cc13xx_cc26xx_sdk_5_40_00_40/source/ti/ble5stack\" --include_path=\"C:/ti/simplelink_cc13xx_cc26xx_sdk_5_40_00_40/source/ti/ble5stack/controller/cc26xx/inc\" --include_path=\"C:/ti/simplelink_cc13xx_cc26xx_sdk_5_40_00_40/source/ti/ble5stack/inc\" --include_path=\"C:/ti/simplelink_cc13xx_cc26xx_sdk_5_40_00_40/source/ti/ble5stack/rom\" --include_path=\"C:/ti/simplelink_cc13xx_cc26xx_sdk_5_40_00_40/source/ti/ble5stack/common/cc26xx\" --include_path=\"C:/ti/simplelink_cc13xx_cc26xx_sdk_5_40_00_40/source/ti/ble5stack/icall/inc\" --include_path=\"C:/ti/simplelink_cc13xx_cc26xx_sdk_5_40_00_40/source/ti/ble5stack/hal/src/target/_common\" --include_path=\"C:/ti/simplelink_cc13xx_cc26xx_sdk_5_40_00_40/source/ti/ble5stack/hal/src/target/_common/cc26xx\" --include_path=\"C:/ti/simplelink_cc13xx_cc26xx_sdk_5_40_00_40/source/ti/ble5stack/hal/src/inc\" --include_path=\"C:/ti/simplelink_cc13xx_cc26xx_sdk_5_40_00_40/source/ti/ble5stack/heapmgr\" --include_path=\"C:/ti/simplelink_cc13xx_cc26xx_sdk_5_40_00_40/source/ti/ble5stack/profiles/dev_info\" --include_path=\"C:/ti/simplelink_cc13xx_cc26xx_sdk_5_40_00_40/source/ti/ble5stack/profiles/simple_profile\" --include_path=\"C:/ti/simplelink_cc13xx_cc26xx_sdk_5_40_00_40/source/ti/ble5stack/icall/src/inc\" --include_path=\"C:/ti/simplelink_cc13xx_cc26xx_sdk_5_40_00_40/source/ti/ble5stack/osal/src/inc\" --include_path=\"C:/ti/simplelink_cc13xx_cc26xx_sdk_5_40_00_40/source/ti/ble5stack/services/src/saddr\" --include_path=\"C:/ti/simplelink_cc13xx_cc26xx_sdk_5_40_00_40/source/ti/ble5stack/services/src/sdata\" --include_path=\"C:/ti/simplelink_cc13xx_cc26xx_sdk_5_40_00_40/source/ti/common/nv\" --include_path=\"C:/ti/simplelink_cc13xx_cc26xx_sdk_5_40_00_40/source/ti/common/cc26xx\" --include_path=\"C:/ti/simplelink_cc13xx_cc26xx_sdk_5_40_00_40/kernel/tirtos/packages\" --include_path=\"C:/ti/simplelink_cc13xx_cc26xx_sdk_5_40_00_40/source/ti/devices/cc13x2_cc26x2\" --include_path=\"C:/ti/simplelink_cc13xx_cc26xx_sdk_5_40_00_40/source/ti/posix/ccs\" --include_path=\"C:/ti/ccs1110/ccs/tools/compiler/ti-cgt-arm_20.2.5.LTS/include\" --define=DeviceFamily_CC26X2 --define=FLASH_ROM_BUILD --define=NVOCMP_NWSAMEITEM=1 -g --c99 --gcc --diag_warning=225 --diag_warning=255 --diag_wrap=off --display_error_number --gen_func_subsections=on --abi=eabi  " "$<"
	@echo 'Finished building: "$<"'
	@echo ' '

configPkg/linker.cmd: build-1950957153 ../simple_central_app.cfg
configPkg/compiler.opt: build-1950957153
configPkg/: build-1950957153


