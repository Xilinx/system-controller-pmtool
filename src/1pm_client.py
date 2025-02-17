# Copyright (C) 2024-2025 Advanced Micro Devices, Inc.  All rights reserved.
# SPDX-License-Identifier: MIT


class PM_Client(object):
    PM = None

    def getvalueall(self):
        """
        Gets the boards's all domain's rails sensor values

        :param : None
        :return: The board's all rails sensor values of the Rail in json formatted
        """
        data = {
            "status": "success",
            "data": {
            "VCK190": [
                {
                    "FPD": {
                        "Rails": [
                            {
                                "VCCINT_PSFP": {
                                    "Voltage": 0.7988,
                                    "Current": 0.178,
                                    "Power": 0.1423
                                }
                            },
                            {
                                "MGTAVCC": {
                                    "Voltage": 0.7988,
                                    "Current": 0.178,
                                    "Power": 0.1423
                                }
                            },
                            {
                                "MGTACTT": {
                                    "Voltage": 0.7988,
                                    "Current": 0.178,
                                    "Power": 0.1423
                                }
                            },
                            {
                                "VCCO_PSDDR_504": {
                                    "Voltage": 0.7988,
                                    "Current": 0.178,
                                    "Power": 0.1423
                                }
                            },
                            {
                                "VCCPMDDRPLL": {
                                    "Voltage": 0.7988,
                                    "Current": 0.178,
                                    "Power": 0.1423
                                }
                            },
                        ],
                        "Total Power": 0.1423
                    }
                },
                {
                    "LPD": {
                        "Rails": [
                            {
                                "VCCPENTLP": {
                                    "Voltage": 0.7988,
                                    "Current": 0.178,
                                    "Power": 0.1423
                                }
                            },
                            {
                                "VCCPSAUX": {
                                    "Voltage": 0.7988,
                                    "Current": 0.178,
                                    "Power": 0.1423
                                }
                            },
                            {
                                "VCCPSPLL": {
                                    "Voltage": 0.7988,
                                    "Current": 0.178,
                                    "Power": 0.1423
                                }
                            },
                            {
                                "VCCOPS": {
                                    "Voltage": 0.7988,
                                    "Current": 0.178,
                                    "Power": 0.1423
                                }
                            },
                            {
                                "VCCOPS3": {
                                    "Voltage": 0.7988,
                                    "Current": 0.178,
                                    "Power": 0.1423
                                }
                            },
                        ],
                        "Total Power": 0.142367
                    }
                },
                {
                    "PLD": {
                        "Rails": [
                            {
                                "VCCINT": {
                                    "Voltage": 0.7988,
                                    "Current": 0.178,
                                    "Power": 0.1423
                                }
                            },
                            {
                                "VCCBRAM": {
                                    "Voltage": 0.7988,
                                    "Current": 0.178,
                                    "Power": 0.1423
                                }
                            },
                            {
                                "VCCAUX": {
                                    "Voltage": 0.7988,
                                    "Current": 0.178,
                                    "Power": 0.1423
                                }
                            },
                            {
                                "VCCTV2": {
                                    "Voltage": 0.7988,
                                    "Current": 0.178,
                                    "Power": 0.1423
                                }
                            },
                            {
                                "VCCTV3": {
                                    "Voltage": 0.792288,
                                    "Current": 0.178,
                                    "Power": 0.1423
                                }
                            },
                        ],
                        "Total Power": 0.1423
                    }
                }
        ]
        },
            "message": "Operation completed successfully."
          }
        return data

    def getboardinfo(self):
        board = {
            "status": "success",
            "data": {
              "Language": 0,
              "Silicon Revision": "",
              "Manufacturing Date": "Thu Apr 28 02:31:00 2022",
              "Manufacturer": "XILINX",
              "Product Name": "VCK190",
              "Board Serial Number": "282203141851",
              "Board Part Number": "043123456",
              "Board Revision": "REV_B01"
            },
            "message": "Operation completed successfully."
          }
        return board
    def listtemperature(self):
        ps_list_temp = {
            "status": "success",
            "data": [
                      "Versal"
                    ],
            "message": "Operation completed successfully."
          }
        return ps_list_temp
    def gettemperature(self, name):
        ps_temp = {
            "status": "success",
            "data": {
                      "TEMP": 30.0,
                      "MIN": 0.0,
                      "MAX_MAX": 0.0,
                      "MIN_MIN": 0.0
                    },
            "message": "Operation completed successfully."
          }
        return ps_temp
    
    def getpowerall(self):
        total_power = {
            "status": "success",
            "data": {
                      "VCK190": {
                        "Power Domains": [
                          {
                            "FPD": {
                              "Power": 0.5539
                            }
                          },
                          {
                            "LPD": {
                              "Power": 0.2545
                            }
                          },
                          {
                            "PLD": {
                              "Power": 9.2938
                            }
                          },
                          {
                            "PMC": {
                              "Power": 0.4543
                            }
                          },
                          {
                            "GTM": {
                              "Power": 0.5312
                            }
                          },
                          {
                            "GTY": {
                              "Power": 0.0605
                            }
                          },
                          {
                            "FMC": {
                              "Power": 0.6335
                            }
                          },
                          {
                            "HBM": {
                              "Power": 0.4582
                            }
                          },
                          {
                            "system": {
                              "Power": 4.9275
                            }
                          },
                          {
                            "chip": {
                              "Power": 16.7441
                            }
                          }
                        ],
                        "Total Power": 33.9115
                      }
                    },
            "message": "Operation completed successfully."
          }
        
        
        return total_power
pm = PM_Client()




