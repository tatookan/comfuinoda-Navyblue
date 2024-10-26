from __future__ import annotations

from typing import TYPE_CHECKING
import inspect  

from comfy.samplers import KSAMPLER
import numpy as np

if TYPE_CHECKING:
    import torch

def advanced_lying_sigma_sampler(
    model: object,
    x: torch.Tensor,
    sigmas: torch.Tensor,
    *,
    sampler: object,
    dishonesty_factor: float,
    start_percent: float,
    end_percent: float,
    smooth_factor: float = 0.5,
    **kwargs: dict,
) -> torch.Tensor:
    start_sigma = round(model.inner_model.inner_model.model_sampling.percent_to_sigma(start_percent), 4)
    end_sigma = round(model.inner_model.inner_model.model_sampling.percent_to_sigma(end_percent), 4)

    def model_wrapper(x: torch.Tensor, sigma: torch.Tensor, **extra_args: dict):
        sigma_float = float(sigma.max().detach().cpu())
        if end_sigma <= sigma_float <= start_sigma:
            adjustment = dishonesty_factor * (0.5 * (1 - np.cos(smooth_factor * np.pi)))
            sigma = sigma * (1.0 + adjustment)
        return model(x, sigma, **extra_args)

    for k in (
        "inner_model",
        "sigmas",
    ):
        if hasattr(model, k):
            setattr(model_wrapper, k, getattr(model, k))

    # Check if denoise_mask is supported by the sampler function
    if 'denoise_mask' in inspect.signature(sampler.sampler_function).parameters:
        return sampler.sampler_function(
            model_wrapper,
            x,
            sigmas,
            denoise_mask=kwargs.get('denoise_mask'),
            **kwargs,
            **sampler.extra_options,
        )
    else:
        return sampler.sampler_function(
            model_wrapper,
            x,
            sigmas,
            **kwargs,
            **sampler.extra_options,
        )

class AdvancedLyingSigmaSamplerNode:
    DESCRIPTION = "高级sigma控制器，使用前最好关闭float rounding并重启comfui,以达到最佳控制效果|For advanced sigma controllers, it is best to turn off float rounding and restart comfui before use for optimal control."
    CATEGORY = "sampling/custom_sampling/advanced_samplers"
    RETURN_TYPES = ("SAMPLER",)
    FUNCTION = "initialize"

    @classmethod
    def INPUT_TYPES(cls) -> dict:
        return {
            "required": {
                "sampler": ("SAMPLER",),
                "dishonesty_factor": (
                    "FLOAT",
                    {
                        "default": -0.1,
                        "min": -1.0,
                        "max": 1.0,
                        "step": 0.001,
                        "tooltip": "默认值-0.1，一般来说这是一个较大值|Default value -0.1, which is generally a larger value."
                    }
                ),
                "start_percent": (
                    "FLOAT",
                    {
                        "default": 0.1,
                        "min": 0.0,
                        "max": 1.0,
                        "step": 0.01,
                        "tooltip": "bilibili@深深蓝hana."
                    }
                ),
                "end_percent": (
                    "FLOAT",
                    {
                        "default": 0.9,
                        "min": 0.0,
                        "max": 1.0,
                        "step": 0.01,
                        "tooltip": "bilibili@深深蓝hana."
                    }
                ),
                "smooth_factor": (
                    "FLOAT",
                    {
                        "default": 0.5,
                        "min": 0.0,
                        "max": 1.0,
                        "step": 0.01,
                        "tooltip": "bilibili@深深蓝hana."
                    }
                ),
            }
        }

    @classmethod
    def initialize(
        cls,
        sampler: object,
        dishonesty_factor: float,
        start_percent: float,
        end_percent: float,
        smooth_factor: float,
    ) -> tuple:
        return (
            KSAMPLER(
                advanced_lying_sigma_sampler,
                extra_options={
                    "sampler": sampler,
                    "dishonesty_factor": dishonesty_factor,
                    "start_percent": start_percent,
                    "end_percent": end_percent,
                    "smooth_factor": smooth_factor,
                },
            ),
        )

NODE_CLASS_MAPPINGS = {
    "AdvancedLyingSigmaSampler": AdvancedLyingSigmaSamplerNode,
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "AdvancedLyingSigmaSampler": "Advanced Lying Sigma Sampler"
}