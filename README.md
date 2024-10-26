# Advanced Lying Sigma Sampler Node

## Introduction
The AdvancedLyingSigmaSampler is an advanced sampler node designed to dynamically adjust the sigma value during the sampling process for finer control. This node modifies the model's behavior by applying an adjustment factor within a specific sigma range, achieving more optimal sampling results.

## Demonstration
### T2M
FLUX: GGUF-Q6K  
Sampler: euler  
Scheduler: beta  
Steps: 20  
Denoise: 1  

| NO | OFF |
|---|---|
| <img src="https://github.com/tatookan/comfuinoda-Navyblue/blob/main/demo/NO.png" alt="Sampler Example" width="300"> | <img src="https://github.com/tatookan/comfuinoda-Navyblue/blob/main/demo/OFF.png" alt="Sampler Example" width="300"> |

| AMINE-ON | AMINE-OFF |
|---|---|
| <img src="https://github.com/tatookan/comfuinoda-Navyblue/blob/main/demo/AMINE-ON.png" alt="Sampler Example" width="300"> | <img src="https://github.com/tatookan/comfuinoda-Navyblue/blob/main/demo/AMINE-ON.png" alt="Sampler Example" width="300"> |

### T2T
FLUX: GGUF-Q6K  
Sampler: euler  
Scheduler: beta  
Steps: 20  
Denoise: 0.5  

| Import Image | On |
|---|---|
| <img src="https://github.com/tatookan/comfuinoda-Navyblue/blob/main/demo/IMAGE.png" alt="Sampler Example" width="300"> | <img src="https://github.com/tatookan/comfuinoda-Navyblue/blob/main/demo/M2M%26NO.png" alt="Sampler Example" width="300"> |

## Usage Instructions
Disable Floating Point Rounding: To achieve the best control effect, it is recommended to disable floating point rounding and restart comfui before using this node.
### Configuration Parameters:
- `dishonesty_factor`: Adjustment factor, default value is -0.1. This is usually a larger value.
- `start_percent`: Percentage at which to start adjusting, default value is 0.1.
- `end_percent`: Percentage at which to stop adjusting, default value is 0.9.
- `smooth_factor`: Smoothing factor, default value is 0.5.

## Precautions
Before using this node, ensure that floating point rounding is disabled and comfui is restarted.
The value of the adjustment factor `dishonesty_factor` has a significant impact on the results. It is recommended to start with the default value and gradually adjust it.

We hope this README is helpful! If you have any questions or suggestions, please feel free to contact us.

# Contact Details
Email: dianyuanan@vip.qq.com  
Join Fan Group: Add WeChat: Miss-Y-s-Honey, and specify your purpose.
