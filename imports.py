import discord
import random
from discord.ext import commands
import openai
import config
import command.hero
from command.hero import get_embed_hero
from command.stage import get_file_stage
from command.omikuji import omikuji
from command.team import team
from command.role_del import role_del