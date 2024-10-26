# Advanced Lying Sigma Sampler Node

## Introduction
The AdvancedLyingSigmaSampler is an advanced sampling node designed to dynamically adjust the sigma value during the sampling process for finer control. This node modifies the model's behavior by applying an adjustment factor within a specific sigma range, achieving more optimal sampling results.

### Usage Instructions
Disable floating-point rounding: To achieve the best control effect, it is recommended to disable floating-point rounding and restart comfui before using this node.
### Configuration Parameters:
- **dishonesty_factor**: Adjustment factor, default value is -0.1. This is usually a larger value.
- **start_percent**: Percentage at which to start adjusting, default value is 0.1.
- **end_percent**: Percentage at which to stop adjusting, default value is 0.9.
- **smooth_factor**: Smoothing factor, default value is 0.5.

## Precautions
Before using this node, ensure that floating-point rounding is disabled and comfui is restarted.
The value of the adjustment factor `dishonesty_factor` significantly impacts the results; it is recommended to start with the default value and gradually adjust as needed.

We hope this README is helpful! If you have any questions or suggestions, please feel free to contact us.

# contact details
 email：dianyuanan@vip.qq.com
 入粉丝群+微信：Miss-Y-s-Honey，注明来意。

