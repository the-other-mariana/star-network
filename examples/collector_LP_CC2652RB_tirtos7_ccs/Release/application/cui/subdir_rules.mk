################################################################################
# Automatically-generated file. Do not edit!
################################################################################

SHELL = cmd.exe

# Each subdirectory must supply rules for building sources it contributes
application/cui/cui.obj: C:/ti/simplelink_cc13xx_cc26xx_sdk_5_40_00_40/source/ti/common/cui/cui.c $(GEN_OPTS) | $(GEN_FILES) $(GEN_MISC_FILES)
	@echo 'Building file: "$<"'
	@echo 'Invoking: Arm Compiler'
	"C:/ti/ccs1110/ccs/tools/compiler/ti-cgt-arm_20.2.5.LTS/bin/armcl" --cmd_file="C:/Users/mariana/workspace_v11/collector_LP_CC2652RB_tirtos7_ccs/application/defines/collector.opts" --cmd_file="C:/Users/mariana/workspace_v11/collector_LP_CC2652RB_tirtos7_ccs/Release/syscfg/ti_154stack_config.opts"  -mv7M4 --code_state=16 --float_support=FPv4SPD16 -me -O4 --opt_for_speed=0 --include_path="C:/Users/mariana/workspace_v11/collector_LP_CC2652RB_tirtos7_ccs" --include_path="C:/Users/mariana/workspace_v11/collector_LP_CC2652RB_tirtos7_ccs/Release" --include_path="C:/Users/mariana/workspace_v11/collector_LP_CC2652RB_tirtos7_ccs/application/collector" --include_path="C:/ti/simplelink_cc13xx_cc26xx_sdk_5_40_00_40/source/ti/ti154stack/common/osal_port" --include_path="C:/ti/simplelink_cc13xx_cc26xx_sdk_5_40_00_40/source/ti/ti154stack/low_level/cc13xx" --include_path="C:/ti/simplelink_cc13xx_cc26xx_sdk_5_40_00_40/source/ti/ti154stack/apps/collector" --include_path="C:/ti/simplelink_cc13xx_cc26xx_sdk_5_40_00_40/source/ti/common/nv" --include_path="C:/ti/simplelink_cc13xx_cc26xx_sdk_5_40_00_40/source/ti/common/cui" --include_path="C:/Users/mariana/workspace_v11/collector_LP_CC2652RB_tirtos7_ccs/application" --include_path="C:/Users/mariana/workspace_v11/collector_LP_CC2652RB_tirtos7_ccs/software_stack/ti15_4stack/osal" --include_path="C:/ti/simplelink_cc13xx_cc26xx_sdk_5_40_00_40/source/ti/ti154stack/apps" --include_path="C:/ti/simplelink_cc13xx_cc26xx_sdk_5_40_00_40/source/ti/ti154stack/common" --include_path="C:/ti/simplelink_cc13xx_cc26xx_sdk_5_40_00_40/source/ti/ti154stack/common/boards" --include_path="C:/ti/simplelink_cc13xx_cc26xx_sdk_5_40_00_40/source/ti/ti154stack/common/util" --include_path="C:/ti/simplelink_cc13xx_cc26xx_sdk_5_40_00_40/source/ti/ti154stack/common/inc" --include_path="C:/ti/simplelink_cc13xx_cc26xx_sdk_5_40_00_40/source/ti/ti154stack/common/stack/src" --include_path="C:/ti/simplelink_cc13xx_cc26xx_sdk_5_40_00_40/source/ti/ti154stack/common/stack/tirtos/inc" --include_path="C:/ti/simplelink_cc13xx_cc26xx_sdk_5_40_00_40/source/ti/ti154stack/common/heapmgr" --include_path="C:/ti/simplelink_cc13xx_cc26xx_sdk_5_40_00_40/source/ti/ti154stack/services/saddr" --include_path="C:/ti/simplelink_cc13xx_cc26xx_sdk_5_40_00_40/source/ti/ti154stack/services/sdata" --include_path="C:/ti/simplelink_cc13xx_cc26xx_sdk_5_40_00_40/source/ti/ti154stack/hal/crypto" --include_path="C:/ti/simplelink_cc13xx_cc26xx_sdk_5_40_00_40/source/ti/ti154stack/hal/platform" --include_path="C:/ti/simplelink_cc13xx_cc26xx_sdk_5_40_00_40/source/ti/ti154stack/hal/rf" --include_path="C:/ti/simplelink_cc13xx_cc26xx_sdk_5_40_00_40/source/ti/ti154stack/fh" --include_path="C:/ti/simplelink_cc13xx_cc26xx_sdk_5_40_00_40/source/ti/ti154stack/high_level" --include_path="C:/ti/simplelink_cc13xx_cc26xx_sdk_5_40_00_40/source/ti/ti154stack/inc" --include_path="C:/ti/simplelink_cc13xx_cc26xx_sdk_5_40_00_40/source/ti/ti154stack/rom" --include_path="C:/ti/simplelink_cc13xx_cc26xx_sdk_5_40_00_40/source/ti/ti154stack/inc/cc13xx" --include_path="C:/ti/simplelink_cc13xx_cc26xx_sdk_5_40_00_40/source/ti/ti154stack/tracer" --include_path="C:/ti/simplelink_cc13xx_cc26xx_sdk_5_40_00_40/source" --include_path="C:/ti/simplelink_cc13xx_cc26xx_sdk_5_40_00_40/source/ti/devices/cc13x2_cc26x2" --include_path="C:/ti/simplelink_cc13xx_cc26xx_sdk_5_40_00_40/source/ti/devices/cc13x2_cc26x2/inc" --include_path="C:/ti/simplelink_cc13xx_cc26xx_sdk_5_40_00_40/source/ti/devices/cc13x2_cc26x2/driverlib" --include_path="C:/ti/simplelink_cc13xx_cc26xx_sdk_5_40_00_40/kernel/tirtos7/packages" --include_path="C:/ti/simplelink_cc13xx_cc26xx_sdk_5_40_00_40/source/ti/posix/ccs" --include_path="C:/ti/ccs1110/ccs/tools/compiler/ti-cgt-arm_20.2.5.LTS/include" --define=TIMAC_ROM_IMAGE_BUILD --define=Board_EXCLUDE_NVS_EXTERNAL_FLASH --define=DeviceFamily_CC26X2 -g --c99 --plain_char=unsigned --diag_warning=225 --diag_warning=255 --diag_wrap=off --display_error_number --gen_func_subsections=on --embedded_constants=on --unaligned_access=on --enum_type=packed --wchar_t=16 --common=on --fp_reassoc=off --sat_reassoc=off --preproc_with_compile --preproc_dependency="application/cui/$(basename $(<F)).d_raw" --include_path="C:/Users/mariana/workspace_v11/collector_LP_CC2652RB_tirtos7_ccs/Release/syscfg" --obj_directory="application/cui" $(GEN_OPTS__FLAG) "$<"
	@echo 'Finished building: "$<"'
	@echo ' '


