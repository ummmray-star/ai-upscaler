from dataclasses import dataclass

class Config:
    # Configuration settings for AI Upscaler
    pass  # Add your settings here

@dataclass
class PresetConfig:
    quality: str
    speed: str

# Define presets for the AI Upscaler
PRESETS = {
    'Fast': PresetConfig(quality='low', speed='high'),
    'Balanced': PresetConfig(quality='medium', speed='medium'),
    'Best': PresetConfig(quality='high', speed='low')
}