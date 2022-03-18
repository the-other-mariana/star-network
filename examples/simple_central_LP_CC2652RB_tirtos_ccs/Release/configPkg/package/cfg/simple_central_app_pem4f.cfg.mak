# invoke SourceDir generated makefile for simple_central_app.pem4f
simple_central_app.pem4f: .libraries,simple_central_app.pem4f
.libraries,simple_central_app.pem4f: package/cfg/simple_central_app_pem4f.xdl
	$(MAKE) -f C:\Users\mariana\workspace_v11\simple_central_LP_CC2652RB_tirtos_ccs/src/makefile.libs

clean::
	$(MAKE) -f C:\Users\mariana\workspace_v11\simple_central_LP_CC2652RB_tirtos_ccs/src/makefile.libs clean

