/*
 *  ======== ti_drivers_config.h ========
 *  Configured TI-Drivers module declarations
 *
 *  The macros defines herein are intended for use by applications which
 *  directly include this header. These macros should NOT be hard coded or
 *  copied into library source code.
 *
 *  Symbols declared as const are intended for use with libraries.
 *  Library source code must extern the correct symbol--which is resolved
 *  when the application is linked.
 *
 *  DO NOT EDIT - This file is generated for the LP_CC2652RB
 *  by the SysConfig tool.
 */
#ifndef ti_drivers_config_h
#define ti_drivers_config_h

#define CONFIG_SYSCONFIG_PREVIEW

#define CONFIG_LP_CC2652RB
#ifndef DeviceFamily_CC26X2
#define DeviceFamily_CC26X2
#endif

#include <ti/devices/DeviceFamily.h>

#include <stdint.h>

/* support C++ sources */
#ifdef __cplusplus
extern "C" {
#endif


/*
 *  ======== CCFG ========
 */
#include DeviceFamily_constructPath(driverlib/osc.h)


/*
 *  ======== AESCCM ========
 */

extern const uint_least8_t                  CONFIG_AESCCM_0_CONST;
#define CONFIG_AESCCM_0                     0
#define CONFIG_TI_DRIVERS_AESCCM_COUNT      1


/*
 *  ======== GPIO ========
 */
/* Owned by CONFIG_DISPLAY_UART as  */
extern const uint_least8_t CONFIG_GPIO_DISPLAY_UART_TX_CONST;
#define CONFIG_GPIO_DISPLAY_UART_TX 3

/* Owned by CONFIG_DISPLAY_UART as  */
extern const uint_least8_t CONFIG_GPIO_DISPLAY_UART_RX_CONST;
#define CONFIG_GPIO_DISPLAY_UART_RX 2

/* Owned by CONFIG_LED_RED as  */
extern const uint_least8_t CONFIG_GPIO_RLED_CONST;
#define CONFIG_GPIO_RLED 6

/* Owned by CONFIG_LED_GREEN as  */
extern const uint_least8_t CONFIG_GPIO_GLED_CONST;
#define CONFIG_GPIO_GLED 7

/* Owned by CONFIG_BTN_LEFT as  */
extern const uint_least8_t CONFIG_GPIO_BTN1_CONST;
#define CONFIG_GPIO_BTN1 13

/* Owned by CONFIG_BTN_RIGHT as  */
extern const uint_least8_t CONFIG_GPIO_BTN2_CONST;
#define CONFIG_GPIO_BTN2 14

/* The range of pins available on this device */
extern const uint_least8_t GPIO_pinLowerBound;
extern const uint_least8_t GPIO_pinUpperBound;

/* LEDs are active high */
#define CONFIG_GPIO_LED_ON  (1)
#define CONFIG_GPIO_LED_OFF (0)

#define CONFIG_LED_ON  (CONFIG_GPIO_LED_ON)
#define CONFIG_LED_OFF (CONFIG_GPIO_LED_OFF)


/*
 *  ======== NVS ========
 */

extern const uint_least8_t              CONFIG_NVSINTERNAL_CONST;
#define CONFIG_NVSINTERNAL              0
#define CONFIG_TI_DRIVERS_NVS_COUNT     1




/*
 *  ======== UART2 ========
 */

/*
 *  TX: DIO3
 *  RX: DIO2
 *  XDS110 UART
 */
extern const uint_least8_t                  CONFIG_DISPLAY_UART_CONST;
#define CONFIG_DISPLAY_UART                 0
#define CONFIG_TI_DRIVERS_UART2_COUNT       1


/*
 *  ======== Button ========
 */

extern const uint_least8_t                  CONFIG_BTN_LEFT_CONST;
#define CONFIG_BTN_LEFT                     0
extern const uint_least8_t                  CONFIG_BTN_RIGHT_CONST;
#define CONFIG_BTN_RIGHT                    1
#define CONFIG_TI_DRIVERS_BUTTON_COUNT      2


/*
 *  ======== LED ========
 */

extern const uint_least8_t              CONFIG_LED_RED_CONST;
#define CONFIG_LED_RED                  0
extern const uint_least8_t              CONFIG_LED_GREEN_CONST;
#define CONFIG_LED_GREEN                1
#define CONFIG_TI_DRIVERS_LED_COUNT     2


/*
 *  ======== Board_init ========
 *  Perform all required TI-Drivers initialization
 *
 *  This function should be called once at a point before any use of
 *  TI-Drivers.
 */
extern void Board_init(void);

/*
 *  ======== Board_initGeneral ========
 *  (deprecated)
 *
 *  Board_initGeneral() is defined purely for backward compatibility.
 *
 *  All new code should use Board_init() to do any required TI-Drivers
 *  initialization _and_ use <Driver>_init() for only where specific drivers
 *  are explicitly referenced by the application.  <Driver>_init() functions
 *  are idempotent.
 */
#define Board_initGeneral Board_init

#ifdef __cplusplus
}
#endif

#endif /* include guard */
