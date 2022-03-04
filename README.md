# Star Network System

A system that connects Texas Instruments' CC2652RB microcontrollers as nodes of a star-shaped network.

## User Guide

1. Download Code Composer Studio (IDE) from: https://www.ti.com/tool/CCSTUDIO

    - Choose the **Single File** option:

    ![img](res/1.png)

    - Before the installation, it is recommended to turn off the PC's antivirus so that the installation goes as ideally.

    - Extract the `.zip` file.

2. All lines below are *suggested* to say OK so that we can proceed to install the IDE program.

![img](res/4.png)

3. In the next prompt, check the three boxes below:

![img](res/5.png)

4. Download the SDK (Software Development Kit) for the CC26x2 boards from: https://www.ti.com/tool/SIMPLELINK-CC13XX-CC26XX-SDK

5. Depending on the OS:

    - For Windows: install the terminal emulator Tera Term (Full Instalation) from: https://tera-term.softonic.com/

    - For Linux (Ubuntu 20.04 was used): 

    ```
    sudo apt install setserial
    sudo apt install cu
    ```

    To get the serial port (COM port) that the board is plugged in, type:

    ```
    sudo setserial -g /dev/ttyS[0123456789]
    ``` 

    And the port (tty0, for example), will be the only one that does not say `UART: unknown`. That is the board's port, and it should have a name `tty[0-9]` or `ttyS[0-9]`. Another option is to type:

    ```
    dmesg | grep tty
    ```

    Now, to finally connect to the board via serial port, type:

    ```
    sudo chmod 666 /dev/ttyS0
    sudo cu -l /dev/ttyS0 -s 115200
    ```

    The last command should output: `Connected.`. To disconnect from the board, type:

    ```
    ~.
    ```

### Collector Node

1. Open Code Composer Studio

2. `Project > Import CCS Projects...`

3. Click on the *Browse* button at the top line's right corner. Navigate to your files to the route of the SDK's folder, which will look something similar to this:

`C:\ti\simplelink_cc13xx_cc26xx_sdk_5_40_00_40\examples\rtos\LP_CC2652RB\ti154stack\collector\tirtos7\ccs`

Once in the `ccs` folder, click on *Select Folder*.

4. A checked box will appear on the prompt, with the project inside the directory just chosen, if it is not checked, please check it.

5. Click on *Finish*.

6. Once the project is loaded in CCS, go to its folder *targetConfigs* and finally click on its file `CC2652RB1F.ccxml`.

7. Make sure that in the left panel the cell that says `CC2652RB1F` is already checked, otherwise it's probably the wrong project.

8. On the right panel, click on *Target Configurations*.

9. In the new panel, click on *Texas Instruments XDS110 USB Debug Probe* and it will display a set of options in the right side. Look for the property *“Debug Probe Selection* and on its menu choose *Select by serial number*. Another text field will appear below it, please type the board's serial number.

10. Click on *Save*.

11. Now, on the CCS's *Project Explorer* View, click on the folder we just loaded from the examples at the SDK's directory, named as the one in the checked box of step 4.

12. Click on the button with the green bug to load the project onto the board.

13. Wait until the console in CCS says:

```
Cortex_M4_0: GEL Output: Memory Map Initialization Complete.
Cortex_M4_0: GEL Output: Memory Map Initialization Complete.
Cortex_M4_0: GEL Output: Board Reset Complete.
```

### Sensor Node

Something almost similar:

1. Open Code Composer Studio

2. `Project > Import CCS Projects...`

3. Click on the *Browse* button at the top line's right corner. Navigate to your files to the route of the SDK's folder, which will look something similar to this:

`C:\ti\simplelink_cc13xx_cc26xx_sdk_5_40_00_40\examples\rtos\LP_CC2652RB\ti154stack\sensor\tirtos7\ccs`

Once in the `ccs` folder, click on *Select Folder*.

4. A checked box will appear on the prompt, with the project inside the directory just chosen, if it is not checked, please check it.

5. Click on *Finish*.

6. Load the project onto the sensor board the same way we did the collector's.