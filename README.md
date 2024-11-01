# Advanced Lying Sigma Sampler Node

## Introduction
the LyingSigmaSampler is a very useful node, as many users find it difficult to understand complex parameters. For these users, they might only need a simple, lightweight, and easy-to-use node. However, I have observed that LyingSigmaSampler does not control the noise mask smoothly enough, or in other words, it cannot control it more precisely. LyingSigmaSampler has a great advantage, of course, other nodes are also great. They can be applied to most models, including SD3.5, and they work well, which is a challenge for users because they have to deal with different noise masks. Therefore, I have added smoothing processing to LyingSigmaSampler in the hope of helping more people.

AdvancedLyingSigmaSampler is an alternative to the LyingSigmaSampler node, a simple advanced sampler node for dynamically adjusting sigma values during sampling for finer control. The node modifies the model behaviour by applying tuning factors within a specific sigma range to achieve more optimal sampling results.

## Demonstration
### T2M
FLUX: GGUF-Q6K  
Sampler: euler  
Scheduler: beta  
Steps: 20  
Denoise: 1  

| ON | OFF |
|---|---|
| <img src="https://github.com/tatookan/comfuinoda-Navyblue/blob/main/demo/NO.png" alt="Sampler Example" width="500"> | <img src="https://github.com/tatookan/comfuinoda-Navyblue/blob/main/demo/OFF.png" alt="Sampler Example" width="500"> |

| AMINE-ON | AMINE-OFF |
|---|---|
| <img src="https://github.com/tatookan/comfuinoda-Navyblue/blob/main/demo/AMINE2-ON_.png" alt="Sampler Example" width="500"> | <img src="https://github.com/tatookan/comfuinoda-Navyblue/blob/main/demo/AMINE2-OFF.png" alt="Sampler Example" width="500"> |

### M2M
FLUX: GGUF-Q6K  
Sampler: euler  
Scheduler: beta  
Steps: 20  
Denoise: 0.5  

| Import Image | Output Image |
|---|---|
| <img src="https://github.com/tatookan/comfuinoda-Navyblue/blob/main/demo/IMAGE.png" alt="Sampler Example" width="500"> | <img src="https://github.com/tatookan/comfuinoda-Navyblue/blob/main/demo/M2M%26NO.png" alt="Sampler Example" width="500"> |

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

## Credits

- Detail Daemon concept and schedule generation function from muerrilla: https://github.com/muerrilla/sd-webui-detail-daemon/
- ComfyUI sampler implementation and schedule interpolation, as well as Lying Sigma Sampler, by https://github.com/blepping/


# Contact Details
Email: dianyuanan@vip.qq.com  
加入我的粉丝群: 联系微信: Miss-Y-s-Honey, 并注明来意
查看我的教程频道 [bilibili@深深蓝hana](https://space.bilibili.com/618554?spm_id_from=333.1007.0.0)
日常作品分享 [douyin@深深蓝](https://www.douyin.com/user/MS4wLjABAAAAJGu7yCfV3XwKoklBX62bivvat3micLxemdDT0FAmdcGfqbuFS3ItsKWKrBt5Hg16?from_tab_name=)
