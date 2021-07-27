import discord 
from discord.ext import commands
from discord.ext.commands import cooldown, BucketType, CommandOnCooldown
import json
import random
from collections import Counter


client = commands.Bot(command_prefix=">")
token = ''

"""
Global Embeds
"""
#Ran out of time embed
ran_out_of_time_em = discord.Embed(
    title = "You ran out of time answering the question! Command cancelled!",
    color = discord.Color.red()
)

cancelled_em = discord.Embed(
    title = "You cancelled the command! Command cancelled!",
    color = discord.Color.red()
)

invalid_reaction_em = discord.Embed(
    title = "You reacted with an invalid response! Command cancelled!",
    color = discord.Color.red()
)




"""
CHARACTER COMMANDS
"""


#createchar command
@client.command()
async def createchar(ctx):

    #Check Functions
    def message_check(message):
        return message.author == ctx.author and message.channel == ctx.channel
    
    def reaction_check(reaction, reactor):
        return reactor == ctx.author 

    user = ctx.author
    users = await get_user_data()
    userids = await get_userids()

    """
    Deciding Faction of the Character
    """
    em1 = discord.Embed(
        title = "What is the faction of your Character?",
        color = discord.Color.blue()
    )
    em1.add_field(name = "Republic - 🟦", value = "** **", inline = False)
    em1.add_field(name = "Separatist - 🟥", value = "** **", inline = False)
    em1.add_field(name = "Bounty Hunter - 🟧", value = "** **", inline = False)
    em1.add_field(name = "Smuggler - 🟨", value = "** **", inline = False)
    em1.add_field(name = "Mandalorian - 🟫", value = "** **", inline = False)
    em1.add_field(name = "Cancel - ❌", value = "** **", inline = False)

    em1.set_thumbnail(
        url = "https://static.wikia.nocookie.net/starwars/images/a/ac/Republic_Emblem_%28unification_wars%29.svg/revision/latest/scale-to-width-down/340?cb=20080311202138"
        )
    
    em1.set_footer(
        icon_url = user.avatar_url, 
        text = f"React with the appropriate reaction. SECONDARY OPTIONS WILL COME AFTER YOU'VE MADE YOUR PRIMARY ALLEGIANCE. Only react after all reactions have been made by the bot. You have 60 seconds to respond"
        )

    #Assigning the message to a variable
    message1 = await ctx.send(embed = em1)

    #Adding reactions to the message
    await message1.add_reaction("🟦")
    await message1.add_reaction("🟥")
    await message1.add_reaction("🟧")
    await message1.add_reaction("🟨")
    await message1.add_reaction("🟫")
    await message1.add_reaction("❌")

    #Listening for the reaction
    try:
        reaction, reactor = await client.wait_for('reaction_add', check = reaction_check, timeout = 60)
        faction_choice1 = str(reaction.emoji)
    except:
        await ctx.send(embed = ran_out_of_time_em)
        return

    if str(reaction.emoji) not in ["🟦","🟥","🟧","🟨","🟫","❌"]:
        await ctx.send(embed = invalid_reaction_em)
        return
    
    if str(reaction.emoji) == "❌":
        await ctx.send(embed = cancelled_em)
        return
    
    faction_dict1 = {
        "🟦" : "Republic",
        "🟥" : "Separatist",
        "🟧" : "Bounty Hunter",
        "🟨" : "Smuggler",
        "🟫" : "Mandalorian"
    }
    
    if faction_choice1 == "🟦":
        republic_faction_choice_em = discord.Embed(
            title = "What is your character's job in the Republic",
            color = discord.Color.blue()
        )
        republic_faction_choice_em.add_field(name = "Clone Trooper - 🟦", value = "** **", inline = False)
        republic_faction_choice_em.add_field(name = "Navy Ensign - 🟥", value = "** **", inline = False)
        republic_faction_choice_em.add_field(name = "Cancel - ❌", value = "** **", inline = False)
        republic_faction_choice_em.set_footer(text = "You have 60 seconds to respond")
        republic_faction_choice_em.set_thumbnail(
            url = "https://static.wikia.nocookie.net/starwars/images/7/7d/Unidentified_clone_naval_officer_%28Kamino%29.png/revision/latest?cb=20130506005454"
            )
        republic_faction_msg = await ctx.send(embed = republic_faction_choice_em)
        await republic_faction_msg.add_reaction("🟦")
        await republic_faction_msg.add_reaction("🟥")
        await republic_faction_msg.add_reaction("❌")

        try:
            reaction, reactor = await client.wait_for('reaction_add', check = reaction_check, timeout = 60)
            faction_choice2 = str(reaction.emoji)
        except:
            await ctx.send(embed = ran_out_of_time_em)
            return
        
        republicDict = {
            "🟦" : "Clone Trooper",
            "🟥" : "Navy Ensign"
        }

        if str(reaction.emoji) not in ["🟦","🟥","❌"]:
            await ctx.send(embed = invalid_reaction_em)
            return

        if faction_choice2 == "❌":
            await ctx.send(embed = cancelled_em)
            return
        
        
        if faction_choice2 == "🟦":
            rep_legion_em = discord.Embed(
                title = "Choose your Clone Trooper Battalion/Legion",
                color = discord.Color.blue()
            )
            rep_legion_em.add_field(name = "501st Legion - 🟦", value = "** **", inline = False)
            rep_legion_em.add_field(name = "21st Nova Corps - 🟪", value = "** **", inline = False)
            rep_legion_em.add_field(name = "91st Reconnaissance Corps - 🟥", value = "** **", inline = False)
            rep_legion_em.add_field(name = "Cancel - ❌", value = "** **", inline = False)
            rep_legion_em.set_footer(text = "You have 60 seconds to respond")

            rep_legion_em.set_thumbnail(
                url = "https://i.pinimg.com/474x/e1/b7/f3/e1b7f3cbcd854fa855ebd202f5341fc3.jpg"
                )

            rep_legion_em_msg = await ctx.send(embed = rep_legion_em)
            await rep_legion_em_msg.add_reaction("🟦")
            await rep_legion_em_msg.add_reaction("🟪")
            await rep_legion_em_msg.add_reaction("🟥")
            await rep_legion_em_msg.add_reaction("❌")

            try:
                reaction, reactor = await client.wait_for('reaction_add', check = reaction_check, timeout = 60)
                rep_legion_reaction = str(reaction.emoji)
            except:
                await ctx.send(embed = ran_out_of_time_em)
                return
            
            if rep_legion_reaction not in ["🟦","🟪","🟥","❌"]:
                await ctx.send(embed = invalid_reaction_em)
                return

            if rep_legion_reaction == "❌":
                await ctx.send(embed = cancelled_em)
                return

            repLegionDict = {
                "🟦" : "501st Legion",
                "🟪" : "21st Nova Corps",
                "🟥" : "91st Reconnaissance Corps"
            }  

            character_name_em = discord.Embed(
                title = "What is the name of your character?",
                color = discord.Color.blue()
            )
            character_name_em.add_field(name = "Clone Name Format:", value = 'CT-#### "{Nickname}". E.g: CT-5384 "Impact"')
            character_name_em.set_thumbnail(
                url = "https://i.pinimg.com/originals/d5/f2/d3/d5f2d39ff9c3ba72f3fd4f96602daac8.jpg"
                )
            character_name_em.set_footer(text = "You have 5 minutes to respond. Send cancel to cancel")

            await ctx.send(embed = character_name_em)
            
            try:
                character_name = str((await client.wait_for('message', check=message_check,timeout=300)).content)
            except:
                await ctx.send(embed = ran_out_of_time_em)
                return
            
            if character_name.lower() == "cancel":
                await ctx.send(embed = cancelled_em)
                return
            
            split_name = character_name.split()

            if len(split_name[0]) != 7:
                invalid_name_em = discord.Embed(
                    title = "You did not enter a valid name!",
                    color = discord.Color.red()
                )
                invalid_name_em.add_field(name = "Clone Name Format:", value = 'CT-#### "{Nickname}". E.g: CT-5384 "Impact"')
                invalid_name_em.set_footer(text = "Your CT number must be 4 numbers! E.g: CT-4921 or CT-9921. Command reset!")
                await ctx.send(embed = invalid_name_em)
                return
            
            remove_other = ["CT-","CC-"]
            clone_nums = split_name[0]
            clone_name2 = split_name[1]
            for remove in remove_other:
                clone_nums = clone_nums.replace(remove,"")
            
            if clone_name2[0] != '"' or clone_name2[-1] != '"':
                non_clone_name = discord.Embed(
                    title = "Invalid Name!",
                    color = discord.Color.red()
                )
                non_clone_name.add_field(name = 'Invalid Name!', value = 'Your nickname must be enclosed in double parenthesis! Example Nickname: "Impact", "Frita", "Stinger"')
                non_clone_name.set_footer(text = "Command reset!")
                await ctx.send(embed = non_clone_name)
                return 
            
            if character_name[:3] != "CT-":
                non_clone_name = discord.Embed(
                    title = "Invalid Name!",
                    color = discord.Color.red()
                )
                non_clone_name.add_field(name = 'Invalid Name!', value = 'Your Identification must start with CT-#### "Nickname"')
                non_clone_name.set_footer(text = "Command reset!")
                await ctx.send(embed = non_clone_name)
                return 
            
            try: 
                clone_nums = int(clone_nums)
                clone_nums = str(clone_nums)
            except:
                non_clone_name = discord.Embed(
                    title = "Invalid Name!",
                    color = discord.Color.red()
                )
                non_clone_name.add_field(name = 'Invalid Name!', value = 'Your Identification number MUST be a number! Example Numbers: CT-1238, CT-5384, CT-8191')
                non_clone_name.set_footer(text = "Command reset!")
                await ctx.send(embed = non_clone_name)
                return 

            for id in userids["userids"]:
                for char in users[id]:
                    if users[id][char]["job"] == "Clone Trooper":
                        their_name = char.split()
                        their_nums = their_name[0]
                        their_name2 = their_name[1]
                        for remove in remove_other:
                            their_nums = their_nums.replace(remove,"")

                        if their_nums == clone_nums and clone_name2 == their_name2:
                            duplicate_name_em = discord.Embed(
                                title = "Duplicate name detected!",
                                color = discord.Color.red()
                            )
                            duplicate_name_em.add_field(name = "Duplicate NAME detected!", value = f"Your entire name is duplicate with {char}")
                            duplicate_name_em.set_footer(text = "Command reset!")
                            await ctx.send(embed = duplicate_name_em)
                            return

                        elif their_nums == clone_nums:
                            duplicate_name_em = discord.Embed(
                                title = "Duplicate name detected!",
                                color = discord.Color.red()
                            )
                            duplicate_name_em.add_field(name = "Duplicate NUMBERS detected!", value = f"Your numbers are duplicate with {char}")
                            duplicate_name_em.set_footer(text = "Command reset!")
                            await ctx.send(embed = duplicate_name_em)
                            return

                        elif clone_name2 == their_name2:
                            duplicate_name_em = discord.Embed(
                                title = "Duplicate name detected!",
                                color = discord.Color.red()
                            )
                            duplicate_name_em.add_field(name = "Duplicate NICKNAME detected!", value = f"Your nickname is duplicate with {char}")
                            duplicate_name_em.set_footer(text = "Command reset!")
                            await ctx.send(embed = duplicate_name_em)
                            return
            
            clone_weapon_choice_em = discord.Embed(
                title = "What is your weapon choice?",
                color = discord.Color.blue()
            )
            clone_weapon_choice_em.add_field(name = "DC-15A - 🟦", value = "** **", inline = False)
            clone_weapon_choice_em.add_field(name = "DC-15S - 🟥", value = "** **", inline = False)
            clone_weapon_choice_em.add_field(name = "Cancel - ❌", value = "** **", inline = False)
            clone_weapon_choice_em.set_footer(text = "You have 30 seconds to respond")

            clone_weapon_choice_em.set_thumbnail(
                url = "https://static.wikia.nocookie.net/starwars/images/3/33/DC-15A_blaster_-_SW_Card_Trader.png/revision/latest?cb=20160710015218"
                )
            
            clone_weapon_choice_msg = await ctx.send(embed = clone_weapon_choice_em)

            await clone_weapon_choice_msg.add_reaction("🟦")
            await clone_weapon_choice_msg.add_reaction("🟥")
            await clone_weapon_choice_msg.add_reaction("❌")


            try:
                reaction, reactor = await client.wait_for('reaction_add', check = reaction_check, timeout = 30)
                weapon_choice = str(reaction.emoji)
            except:
                await ctx.send(embed = ran_out_of_time_em)
                return
            
            if weapon_choice == "❌":
                await ctx.send(embed = cancelled_em)
                return
            
            if str(reaction.emoji) not in ["🟦","🟥","❌"]:
                await ctx.send(embed = invalid_reaction_em)
                return
            
            weapon_dict = {
                "🟦" : "DC-15A",
                "🟥" : "DC-15S"
            }

            """
            End Details
            """
            faction = faction_dict1[faction_choice1]
            job = republicDict[faction_choice2]
            legion = repLegionDict[rep_legion_reaction]
            weapon_choice = [weapon_dict[weapon_choice]]
            armor = "Standard Phase 2 Clone Trooper Armor"
            items = ["Thermal Detonator", "Healthpack"]
            roles = [faction,job,legion]
            species = "human"
            money = 0
            is_character = "no"
            ships = []

            final_char_layout = discord.Embed(
                title = f"This is your Character: {character_name}",
                color = discord.Color.blue()
            )

            final_char_layout.add_field(name = "Faction", value = faction, inline = False)
            final_char_layout.add_field(name = "Job", value = job, inline = True)
            final_char_layout.add_field(name = "Legion", value = legion, inline = False)
            final_char_layout.add_field(name = "Weapon", value = weapon_choice, inline = True)
            final_char_layout.add_field(name = "Armor", value = armor, inline = False)
            final_char_layout.add_field(name = "Items", value = items, inline = False)
            final_char_layout.add_field(name = "Ships", value = "None", inline = False)
            final_char_layout.add_field(name = "Money", value = money, inline = True)
            final_char_layout.add_field(name = "Species", value = species, inline = True)
            final_char_layout.set_footer(icon_url = user.avatar_url, text = "React with '✅' if you are content with your character or '❌' to cancel. You have 60 seconds to respond")

            final_char_message = await ctx.send(embed = final_char_layout)

            await final_char_message.add_reaction("✅")
            await final_char_message.add_reaction("❌")

            try:
                reaction, reactor = await client.wait_for('reaction_add', check = reaction_check, timeout = 60)
                go_ahead = str(reaction.emoji)
            except:
                await ctx.send(embed = ran_out_of_time_em)
                return
            
            if go_ahead == "❌":
                await ctx.send(embed = cancelled_em)
                return
            
            if str(reaction.emoji) not in ["✅","❌"]:
                await ctx.send(embed = invalid_reaction_em)
                return
            
            if True:
                if str(user.id) in users:
                    users[str(user.id)][character_name] = {}
                    users[str(user.id)][character_name]["faction"] = faction
                    users[str(user.id)][character_name]["job"] = job
                    users[str(user.id)][character_name]["legion"] = legion
                    users[str(user.id)][character_name]["weapons"] = weapon_choice
                    users[str(user.id)][character_name]["armor"] = armor
                    users[str(user.id)][character_name]["items"] = items 
                    users[str(user.id)][character_name]["species"] = species
                    users[str(user.id)][character_name]["money"] = 0
                    users[str(user.id)][character_name]["roles"] = roles
                    users[str(user.id)][character_name]["is_character"] = is_character
                    users[str(user.id)][character_name]["ships"] = ships
                    users[str(user.id)][character_name]["units"] = []
                else:
                    users[str(user.id)] = {}
                    users[str(user.id)][character_name] = {}
                    users[str(user.id)][character_name]["faction"] = faction
                    users[str(user.id)][character_name]["job"] = job
                    users[str(user.id)][character_name]["legion"] = legion
                    users[str(user.id)][character_name]["weapons"] = weapon_choice
                    users[str(user.id)][character_name]["armor"] = armor
                    users[str(user.id)][character_name]["items"] = items 
                    users[str(user.id)][character_name]["species"] = species
                    users[str(user.id)][character_name]["money"] = 0
                    users[str(user.id)][character_name]["roles"] = roles
                    users[str(user.id)][character_name]["is_character"] = is_character
                    users[str(user.id)][character_name]["ships"] = ships
                    users[str(user.id)][character_name]["units"] = []

            with open("users.json", "w") as f:
                json.dump(users,f,sort_keys=True, indent=4, separators=(',', ': '))
            
            if str(user.id) not in userids["userids"]:
                userids["userids"].append(str(user.id))
                with open("userids.json", "w") as f:
                    json.dump(userids,f,sort_keys=True, indent=4, separators=(',', ': '))
            
            data_success = discord.Embed(
                title = "Data Created Successfully!",
                color = discord.Color.green()
            )
            await ctx.send(embed = data_success)
            return
            

        elif faction_choice2 == "🟥":

            character_name_em = discord.Embed(
                title = "What is the name of your character?",
                color = discord.Color.blue()
            )
            character_name_em.add_field(name = "Navy Ensign Format:", value = 'Ensign <Name>. e.g: Ensign Rendix, Ensign Colt, Ensign Mordoe')
            character_name_em.set_footer(text = "You have 5 minutes to respond. Your name can only have one word after 'Ensign'. Send cancel to cancel")

            await ctx.send(embed = character_name_em)

            try:
                character_name = str((await client.wait_for('message', check=message_check,timeout=300)).content)
            except:
                await ctx.send(embed = ran_out_of_time_em)
                return
            
            new_char_name = character_name.split()

            if character_name.lower() == "cancel":
                await ctx.send(embed = cancelled_em)
                return
                        
            if new_char_name[0] != "Ensign":
                invalid_name_em = discord.Embed(
                    title = "You did not enter a valid name!",
                    color = discord.Color.red()
                )
                invalid_name_em.add_field(name = "INVALID RANK AT THE BEGINNING!", value = "Proper Names: Ensign Rendix, Ensign Colt, Ensign Mordoe.")
                await ctx.send(embed = invalid_name_em)
                return

            if len(new_char_name) != 2:
                invalid_name_em = discord.Embed(
                    title = "You did not enter a valid name!",
                    color = discord.Color.red()
                )
                invalid_name_em.add_field(name = "Your name can only have 1 word after Ensign!", value = "e.g: Ensign Rendix, Ensign Colt, Ensign Mordoe.")
                await ctx.send(embed = invalid_name_em)
                return

            for name_char in character_name:
                if name_char == '"' or name_char == "'":
                    invalid_name_em = discord.Embed(
                        title = "You did not enter a valid name!",
                        color = discord.Color.red()
                    )
                    invalid_name_em.add_field(name = 'DOUBLE/SINGLE QUOTES DETECTED IN NAME, PLEASE REMOVE THEM!', value = "Proper Names: Ensign Rendix, Ensign Colt, Ensign Mordoe.")
                    await ctx.send(embed = invalid_name_em)
                    return
            
            for id in userids["userids"]:
                for char in users[id]:
                    if users[id][char]["legion"] == "Republic Navy" or users[id][char]["legion"] == "Separatist Navy":
                        other_char_name = char.split()
                        if new_char_name[1].lower() == other_char_name[1].lower():
                            duplicate_name_em = discord.Embed(
                                title = "Duplicate name detected!",
                                color = discord.Color.red()
                            )
                            duplicate_name_em.add_field(name = "DUPlICATE NAME DETECTED!", value = f"Your name is duplicate with {char}")
                            await ctx.send(embed = duplicate_name_em)
                            return

            faction = faction_dict1[faction_choice1]
            job = republicDict[faction_choice2]
            legion = "Republic Navy"
            weapon_choice = ["DC-17"]
            armor = "None"
            items = ["Datapad","Comms"]
            roles = [faction,job,legion]
            species = "human"
            money = 0
            is_character = "no"
            ships = []

            final_char_layout = discord.Embed(
                title = f"This is your Character: {character_name}",
                color = discord.Color.blue()
            )

            final_char_layout.add_field(name = "Faction", value = faction, inline = False)
            final_char_layout.add_field(name = "Job", value = job, inline = True)
            final_char_layout.add_field(name = "Legion", value = legion, inline = False)
            final_char_layout.add_field(name = "Weapon", value = weapon_choice, inline = True)
            final_char_layout.add_field(name = "Armor", value = armor, inline = False)
            final_char_layout.add_field(name = "Items", value = items, inline = False)
            final_char_layout.add_field(name = "Ships", value = "None", inline = False)
            final_char_layout.add_field(name = "Money", value = money, inline = True)
            final_char_layout.add_field(name = "Species", value = species, inline = True)
            final_char_layout.set_footer(icon_url = user.avatar_url, text = "React with '✅' if you are content with your character or '❌' to cancel. You have 60 seconds to respond")

            final_char_message = await ctx.send(embed = final_char_layout)

            await final_char_message.add_reaction("✅")
            await final_char_message.add_reaction("❌")

            try:
                reaction, reactor = await client.wait_for('reaction_add', check = reaction_check, timeout = 60)
                go_ahead = str(reaction.emoji)
            except:
                await ctx.send(embed = ran_out_of_time_em)
                return
            
            if go_ahead == "❌":
                await ctx.send(embed = cancelled_em)
                return
            
            if str(reaction.emoji) not in ["✅","❌"]:
                await ctx.send(embed = invalid_reaction_em)
                return
            
            if True:
                if str(user.id) in users:
                    users[str(user.id)][character_name] = {}
                    users[str(user.id)][character_name]["faction"] = faction
                    users[str(user.id)][character_name]["job"] = job
                    users[str(user.id)][character_name]["legion"] = legion
                    users[str(user.id)][character_name]["weapons"] = weapon_choice
                    users[str(user.id)][character_name]["armor"] = armor
                    users[str(user.id)][character_name]["items"] = items 
                    users[str(user.id)][character_name]["species"] = species
                    users[str(user.id)][character_name]["money"] = 0
                    users[str(user.id)][character_name]["roles"] = roles
                    users[str(user.id)][character_name]["is_character"] = is_character
                    users[str(user.id)][character_name]["ships"] = ships
                    users[str(user.id)][character_name]["units"] = []
                else:
                    users[str(user.id)] = {}
                    users[str(user.id)][character_name] = {}
                    users[str(user.id)][character_name]["faction"] = faction
                    users[str(user.id)][character_name]["job"] = job
                    users[str(user.id)][character_name]["legion"] = legion
                    users[str(user.id)][character_name]["weapons"] = weapon_choice
                    users[str(user.id)][character_name]["armor"] = armor
                    users[str(user.id)][character_name]["items"] = items 
                    users[str(user.id)][character_name]["species"] = species
                    users[str(user.id)][character_name]["money"] = 0
                    users[str(user.id)][character_name]["roles"] = roles
                    users[str(user.id)][character_name]["is_character"] = is_character
                    users[str(user.id)][character_name]["ships"] = ships
                    users[str(user.id)][character_name]["units"] = []
                
                with open("users.json", "w") as f:
                    json.dump(users,f,sort_keys=True, indent=4, separators=(',', ': '))
            
                if str(user.id) not in userids["userids"]:
                    userids["userids"].append(str(user.id))
                    with open("userids.json", "w",sort_keys=True, indent=4, separators=(',', ': ')) as f:
                        json.dump(userids,f)
                
                data_success = discord.Embed(
                    title = "Data Created Successfully!",
                    color = discord.Color.green()
                )

                await ctx.send(embed = data_success)
                return
                
    elif faction_choice1 == "🟥":
        separatist_faction_choice_em = discord.Embed(
            title = "What is your character's job in the Separatist Alliance?",
            color = discord.Color.blue()
        )            
        separatist_faction_choice_em.add_field(name = "B1 Battle Droid - 🟦", value = "** **", inline = False)
        separatist_faction_choice_em.add_field(name = "B2 Super Battle Droid - 🟥", value = "** **", inline = False)
        separatist_faction_choice_em.add_field(name = "BX-Commando Droid - 🟧", value = "** **", inline = False)
        separatist_faction_choice_em.add_field(name = "Separatist Organic Soldier - 🟨", value = "** **", inline = False)
        separatist_faction_choice_em.add_field(name = "Separatist Organic Navy Ensign - 🟫", value = "** **", inline = False)
        separatist_faction_choice_em.add_field(name = "Cancel - ❌", value = "** **", inline = False)
        separatist_faction_choice_em.set_footer(text = "You have 60 seconds to respond")

        separatist_faction_choice_em.set_thumbnail(url = "https://i.pinimg.com/originals/02/4f/73/024f7332afb0edfd53cc5530659bfa27.png")

        separatist_faction_msg = await ctx.send(embed = separatist_faction_choice_em)

        await separatist_faction_msg.add_reaction("🟦")
        await separatist_faction_msg.add_reaction("🟥")
        await separatist_faction_msg.add_reaction("🟧")
        await separatist_faction_msg.add_reaction("🟨")
        await separatist_faction_msg.add_reaction("🟫")
        await separatist_faction_msg.add_reaction("❌")

        try:
            reaction, reactor = await client.wait_for('reaction_add', check = reaction_check, timeout = 60)
            faction_choice2 = str(reaction.emoji)
        except:
            await ctx.send(embed = ran_out_of_time_em)
            return
        
        separatistDict = {
            "🟦" : "B1 Battle Droid",
            "🟥" : "B2 Super Battle Droid",
            "🟧" : "BX-Commando Droid",
            "🟨" : "Separatist Organic Soldier",
            "🟫" : "Separatist Organic Navy Ensign"
        }

        if str(reaction.emoji) not in ["🟦","🟥","🟧","🟨","🟫","❌"]:
            await ctx.send(embed = invalid_reaction_em)
            return

        if faction_choice2 == "❌":
            await ctx.send(embed = cancelled_em)
            return
        
        if faction_choice2 == "🟦":
            character_name_em = discord.Embed(
                title = "What is the name of your character?",
                color = discord.Color.blue()
            )
            character_name_em.add_field(
                name = "B1 Battle Droid Format:", 
                value = 'B1-####. e.g: B1-3910, B1-9910, B1-8291, B1-5384'
                )
            character_name_em.set_footer(
                text = "You have 5 minutes to respond. Send cancel to cancel"
                )

            await ctx.send(embed = character_name_em)

            try:
                character_name = str((await client.wait_for('message', check=message_check, timeout=300)).content)
            except:
                await ctx.send(embed = ran_out_of_time_em)
                return
            
            if character_name.lower() == "cancel":
                await ctx.send(embed = cancelled_em)
                return
            
            if len(character_name) != 7:
                invalid_name_em = discord.Embed(
                    title = "You did not enter a valid name!",
                    color = discord.Color.red()
                )
                invalid_name_em.add_field(
                    name = "INVALID NAME!", 
                    value = "Proper Format: B1-####, e.g: B1-3910, B1-9910, B1-8291, B1-5384"
                    )
                invalid_name_em.set_footer(text = "Command reset!")
                await ctx.send(embed = invalid_name_em)
                return
            
            if character_name[:3] != "B1-":
                invalid_name_em = discord.Embed(
                    title = "You did not enter a valid name!",
                    color = discord.Color.red()
                )
                invalid_name_em.add_field(
                    name = "INVALID NAME!", 
                    value = "Proper Format: B1-####, e.g: B1-3910, B1-9910, B1-8291, B1-5384"
                    )
                invalid_name_em.set_footer(text = "Command reset!")
                await ctx.send(embed = invalid_name_em)
                return
            
            b1_nums = character_name.replace("B1-","")

            try: 
                b1_nums = int(b1_nums)
                b1_nums = str(b1_nums)
            except:
                non_clone_name = discord.Embed(
                    title = "Invalid Name!",
                    color = discord.Color.red()
                )
                non_clone_name.add_field(
                    name = 'INVALID NAME!', 
                    value = 'Your Identification number MUST be a number! Example Numbers: B1-3910, B1-9910, B1-8291, B1-5384')
                non_clone_name.set_footer(text = "Command reset!")
                await ctx.send(embed = non_clone_name)
                return 

                invalid_name_em = discord.Embed(
                    title = "You did not enter a valid name!",
                    color = discord.Color.red()
                )

                invalid_name_em.add_field(
                    name = "INVALID NAME!", 
                    value = "Proper Format: B1-####, e.g: B1-3910, B1-9910, B1-8291, B1-5384"
                    )
                await ctx.send(embed = invalid_name_em)
                return
            
            for id in userids["userids"]:
                for char in users[id]:
                    if users[id][char]["faction"] == "Separatist":
                        remove_other = ["B1-", "B2-","BX-"]
                        for remove in remove_other:
                            char_name = char.replace(remove,"")
                            if char_name == b1_nums:
                                duplicate_name_em = discord.Embed(
                                    title = "Duplicate name detected!",
                                    color = discord.Color.red()
                                )
                                duplicate_name_em.add_field(name = "Duplicate NAME detected!", value = f"Your entire name is duplicate with {char}")
                                duplicate_name_em.set_footer(text = "Command reset!")
                                await ctx.send(embed = duplicate_name_em)
                                return
            
            faction = faction_dict1[faction_choice1]
            job = separatistDict[faction_choice2]
            legion = "None"
            weapon_choice = ["E-5"]
            armor = "Standard B1 Droid Armor Plating"
            items = ["Manual Repair Kit", "Thermal Detonator"]
            roles = [faction,job]
            species = "droid"
            money = 0
            is_character = "no"
            ships = []

            final_char_layout = discord.Embed(
                title = f"This is your Character: {character_name}",
                color = discord.Color.blue()
            )

            final_char_layout.add_field(name = "Faction", value = faction, inline = False)
            final_char_layout.add_field(name = "Job", value = job, inline = True)
            final_char_layout.add_field(name = "Legion", value = legion, inline = False)
            final_char_layout.add_field(name = "Weapon", value = weapon_choice, inline = True)
            final_char_layout.add_field(name = "Armor", value = armor, inline = False)
            final_char_layout.add_field(name = "Items", value = items, inline = False)
            final_char_layout.add_field(name = "Ships", value = "None", inline = False)
            final_char_layout.add_field(name = "Money", value = money, inline = True)
            final_char_layout.add_field(name = "Species", value = species, inline = True)
            final_char_layout.set_footer(icon_url = user.avatar_url, text = "React with '✅' if you are content with your character or '❌' to cancel. You have 60 seconds to respond")

            final_char_message = await ctx.send(embed = final_char_layout)

            await final_char_message.add_reaction("✅")
            await final_char_message.add_reaction("❌")

            try:
                reaction, reactor = await client.wait_for('reaction_add', check = reaction_check, timeout = 60)
                go_ahead = str(reaction.emoji)
            except:
                await ctx.send(embed = ran_out_of_time_em)
                return
            
            if go_ahead == "❌":
                await ctx.send(embed = cancelled_em)
                return
            
            if str(reaction.emoji) not in ["✅","❌"]:
                await ctx.send(embed = invalid_reaction_em)
                return
            
            if True:
                if str(user.id) in users:
                    users[str(user.id)][character_name] = {}
                    users[str(user.id)][character_name]["faction"] = faction
                    users[str(user.id)][character_name]["job"] = job
                    users[str(user.id)][character_name]["legion"] = legion
                    users[str(user.id)][character_name]["weapons"] = weapon_choice
                    users[str(user.id)][character_name]["armor"] = armor
                    users[str(user.id)][character_name]["items"] = items 
                    users[str(user.id)][character_name]["species"] = species
                    users[str(user.id)][character_name]["money"] = 0
                    users[str(user.id)][character_name]["roles"] = roles
                    users[str(user.id)][character_name]["is_character"] = is_character
                    users[str(user.id)][character_name]["ships"] = ships
                    users[str(user.id)][character_name]["units"] = []
                else:
                    users[str(user.id)] = {}
                    users[str(user.id)][character_name] = {}
                    users[str(user.id)][character_name]["faction"] = faction
                    users[str(user.id)][character_name]["job"] = job
                    users[str(user.id)][character_name]["legion"] = legion
                    users[str(user.id)][character_name]["weapons"] = weapon_choice
                    users[str(user.id)][character_name]["armor"] = armor
                    users[str(user.id)][character_name]["items"] = items 
                    users[str(user.id)][character_name]["species"] = species
                    users[str(user.id)][character_name]["money"] = 0
                    users[str(user.id)][character_name]["roles"] = roles
                    users[str(user.id)][character_name]["is_character"] = is_character
                    users[str(user.id)][character_name]["ships"] = ships
                    users[str(user.id)][character_name]["units"] = []

            with open("users.json", "w") as f:
                json.dump(users,f,sort_keys=True, indent=4, separators=(',', ': '))
            
            if str(user.id) not in userids["userids"]:
                userids["userids"].append(str(user.id))
                with open("userids.json", "w",sort_keys=True, indent=4, separators=(',', ': ')) as f:
                    json.dump(userids,f)
            
            data_success = discord.Embed(
                title = "Data Created Successfully!",
                color = discord.Color.green()
            )
            await ctx.send(embed = data_success)
            return

        elif faction_choice2 == "🟥":
            character_name_em = discord.Embed(
                title = "What is the name of your character?",
                color = discord.Color.blue()
            )
            character_name_em.add_field(
                name = "B2 Battle Droid Format:", 
                value = 'B2-####. e.g: B2-3910, B2-9910, B2-8291, B2-5384'
                )
            character_name_em.set_footer(
                text = "You have 5 minutes to respond. Send cancel to cancel"
                )

            await ctx.send(embed = character_name_em)

            try:
                character_name = str((await client.wait_for('message', check=message_check, timeout=300)).content)
            except:
                await ctx.send(embed = ran_out_of_time_em)
                return
            
            if character_name.lower() == "cancel":
                await ctx.send(embed = cancelled_em)
                return
            
            if len(character_name) != 7:
                invalid_name_em = discord.Embed(
                    title = "You did not enter a valid name!",
                    color = discord.Color.red()
                )
                invalid_name_em.add_field(
                    name = "INVALID NAME!", 
                    value = "Proper Format: B2-####, e.g: B2-3910, B2-9910, B2-8291, B2-5384"
                    )
                invalid_name_em.set_footer(text = "Command reset!")
                await ctx.send(embed = invalid_name_em)
                return
            
            if character_name[:3] != "B2-":
                invalid_name_em = discord.Embed(
                    title = "You did not enter a valid name!",
                    color = discord.Color.red()
                )
                invalid_name_em.add_field(
                    name = "INVALID NAME!", 
                    value = "Proper Format: B2-####, e.g: B2-3910, B2-9910, B2-8291, B2-5384"
                    )
                invalid_name_em.set_footer(text = "Command reset!")
                await ctx.send(embed = invalid_name_em)
                return
            
            b1_nums = character_name.replace("B2-","")

            try: 
                b1_nums = int(b1_nums)
                b1_nums = str(b1_nums)
            except:
                non_clone_name = discord.Embed(
                    title = "Invalid Name!",
                    color = discord.Color.red()
                )
                non_clone_name.add_field(
                    name = 'INVALID NAME!', 
                    value = 'Your Identification number MUST be a number! Example Numbers: B2-3910, B2-9910, B2-8291, B2-5384')
                non_clone_name.set_footer(text = "Command reset!")
                await ctx.send(embed = non_clone_name)
                return 

                invalid_name_em = discord.Embed(
                    title = "You did not enter a valid name!",
                    color = discord.Color.red()
                )

                invalid_name_em.add_field(
                    name = "INVALID NAME!", 
                    value = "Proper Format: B2-####, e.g: B2-3910, B2-9910, B2-8291, B2-5384"
                    )
                await ctx.send(embed = invalid_name_em)
                return
            
            for id in userids["userids"]:
                for char in users[id]:
                    if users[id][char]["faction"] == "Separatist":
                        remove_other = ["B1-", "B2-","BX-"]
                        for remove in remove_other:
                            char_name = char.replace(remove,"")
                            if char_name == b1_nums:
                                duplicate_name_em = discord.Embed(
                                    title = "Duplicate name detected!",
                                    color = discord.Color.red()
                                )
                                duplicate_name_em.add_field(name = "Duplicate NAME detected!", value = f"Your entire name is duplicate with {char}")
                                duplicate_name_em.set_footer(text = "Command reset!")
                                await ctx.send(embed = duplicate_name_em)
                                return
            
            faction = faction_dict1[faction_choice1]
            job = separatistDict[faction_choice2]
            legion = "None"
            weapon_choice = ["Wrist Rocket", "B2 Arm Blaster"]
            armor = "Standard B2 Droid Armor Plating"
            items = ["Manual Repair Kit"]
            roles = [faction,job]
            species = "droid"
            money = 0
            is_character = "no"
            ships = []

            final_char_layout = discord.Embed(
                title = f"This is your Character: {character_name}",
                color = discord.Color.blue()
            )

            final_char_layout.add_field(name = "Faction", value = faction, inline = False)
            final_char_layout.add_field(name = "Job", value = job, inline = True)
            final_char_layout.add_field(name = "Legion", value = legion, inline = False)
            final_char_layout.add_field(name = "Weapon", value = weapon_choice, inline = True)
            final_char_layout.add_field(name = "Armor", value = armor, inline = False)
            final_char_layout.add_field(name = "Items", value = items, inline = False)
            final_char_layout.add_field(name = "Ships", value = "None", inline = False)
            final_char_layout.add_field(name = "Money", value = money, inline = True)
            final_char_layout.add_field(name = "Species", value = species, inline = True)
            final_char_layout.set_footer(icon_url = user.avatar_url, text = "React with '✅' if you are content with your character or '❌' to cancel. You have 60 seconds to respond")

            final_char_message = await ctx.send(embed = final_char_layout)

            await final_char_message.add_reaction("✅")
            await final_char_message.add_reaction("❌")

            try:
                reaction, reactor = await client.wait_for('reaction_add', check = reaction_check, timeout = 60)
                go_ahead = str(reaction.emoji)
            except:
                await ctx.send(embed = ran_out_of_time_em)
                return
            
            if go_ahead == "❌":
                await ctx.send(embed = cancelled_em)
                return
            
            if str(reaction.emoji) not in ["✅","❌"]:
                await ctx.send(embed = invalid_reaction_em)
                return
            
            if True:
                if str(user.id) in users:
                    users[str(user.id)][character_name] = {}
                    users[str(user.id)][character_name]["faction"] = faction
                    users[str(user.id)][character_name]["job"] = job
                    users[str(user.id)][character_name]["legion"] = legion
                    users[str(user.id)][character_name]["weapons"] = weapon_choice
                    users[str(user.id)][character_name]["armor"] = armor
                    users[str(user.id)][character_name]["items"] = items 
                    users[str(user.id)][character_name]["species"] = species
                    users[str(user.id)][character_name]["money"] = 0
                    users[str(user.id)][character_name]["roles"] = roles
                    users[str(user.id)][character_name]["is_character"] = is_character
                    users[str(user.id)][character_name]["ships"] = ships
                    users[str(user.id)][character_name]["units"] = []
                else:
                    users[str(user.id)] = {}
                    users[str(user.id)][character_name] = {}
                    users[str(user.id)][character_name]["faction"] = faction
                    users[str(user.id)][character_name]["job"] = job
                    users[str(user.id)][character_name]["legion"] = legion
                    users[str(user.id)][character_name]["weapons"] = weapon_choice
                    users[str(user.id)][character_name]["armor"] = armor
                    users[str(user.id)][character_name]["items"] = items 
                    users[str(user.id)][character_name]["species"] = species
                    users[str(user.id)][character_name]["money"] = 0
                    users[str(user.id)][character_name]["roles"] = roles
                    users[str(user.id)][character_name]["is_character"] = is_character
                    users[str(user.id)][character_name]["ships"] = ships
                    users[str(user.id)][character_name]["units"] = []

            with open("users.json", "w") as f:
                json.dump(users,f,sort_keys=True, indent=4, separators=(',', ': '))
            
            if str(user.id) not in userids["userids"]:
                userids["userids"].append(str(user.id))
                with open("userids.json", "w") as f:
                    json.dump(userids,f,sort_keys=True, indent=4, separators=(',', ': '))
            
            data_success = discord.Embed(
                title = "Data Created Successfully!",
                color = discord.Color.green()
            )
            await ctx.send(embed = data_success)
            return

        elif faction_choice2 == "🟧":
            character_name_em = discord.Embed(
                title = "What is the name of your character?",
                color = discord.Color.blue()
            )
            character_name_em.add_field(
                name = "BX Battle Droid Format:", 
                value = 'BX-####. e.g: BX-3910, BX-9910, BX-8291, BX-5384'
                )
            character_name_em.set_footer(
                text = "You have 5 minutes to respond. Send cancel to cancel"
                )

            await ctx.send(embed = character_name_em)

            try:
                character_name = str((await client.wait_for('message', check=message_check, timeout=300)).content)
            except:
                await ctx.send(embed = ran_out_of_time_em)
                return

            if character_name.lower() == "cancel":
                await ctx.send(embed = cancelled_em)
                return
            
            if len(character_name) != 7:
                invalid_name_em = discord.Embed(
                    title = "You did not enter a valid name!",
                    color = discord.Color.red()
                )
                invalid_name_em.add_field(
                    name = "INVALID NAME!", 
                    value = "Proper Format: BX-####, e.g: BX-3910, BX-9910, BX-8291, BX-5384"
                    )
                invalid_name_em.set_footer(text = "Command reset!")
                await ctx.send(embed = invalid_name_em)
                return
            
            if character_name[:3] != "BX-":
                invalid_name_em = discord.Embed(
                    title = "You did not enter a valid name!",
                    color = discord.Color.red()
                )
                invalid_name_em.add_field(
                    name = "INVALID NAME!", 
                    value = "Proper Format: BX-####, e.g: BX-3910, BX-9910, BX-8291, BX-5384"
                    )
                invalid_name_em.set_footer(text = "Command reset!")
                await ctx.send(embed = invalid_name_em)
                return
            
            b1_nums = character_name.replace("BX-","")

            try: 
                b1_nums = int(b1_nums)
                b1_nums = str(b1_nums)
            except:
                non_clone_name = discord.Embed(
                    title = "Invalid Name!",
                    color = discord.Color.red()
                )
                non_clone_name.add_field(
                    name = 'INVALID NAME!', 
                    value = 'Your Identification number MUST be a number! Example Numbers: B1-3910, B1-9910, B1-8291, B1-5384')
                non_clone_name.set_footer(text = "Command reset!")
                await ctx.send(embed = non_clone_name)
                return 

                invalid_name_em = discord.Embed(
                    title = "You did not enter a valid name!",
                    color = discord.Color.red()
                )

                invalid_name_em.add_field(
                    name = "INVALID NAME!", 
                    value = "Proper Format: B1-####, e.g: B1-3910, B1-9910, B1-8291, B1-5384"
                    )
                await ctx.send(embed = invalid_name_em)
                return
            
            for id in userids["userids"]:
                for char in users[id]:
                    if users[id][char]["faction"] == "Separatist":
                        remove_other = ["B1-", "B2-","BX-"]
                        for remove in remove_other:
                            char_name = char.replace(remove,"")
                            if char_name == b1_nums:
                                duplicate_name_em = discord.Embed(
                                    title = "Duplicate name detected!",
                                    color = discord.Color.red()
                                )
                                duplicate_name_em.add_field(name = "Duplicate NAME detected!", value = f"Your entire name is duplicate with {char}")
                                duplicate_name_em.set_footer(text = "Command reset!")
                                await ctx.send(embed = duplicate_name_em)
                                return
            
            faction = faction_dict1[faction_choice1]
            job = separatistDict[faction_choice2]
            legion = "None"
            weapon_choice = ["E-5", "Vibroblade"]
            armor = "Standard BX Droid Armor Plating"
            items = ["Manual Repair Kit", "Smoke Bomb"]
            roles = [faction,job]
            species = "droid"
            money = 0
            is_character = "no"
            ships = []

            final_char_layout = discord.Embed(
                title = f"This is your Character: {character_name}",
                color = discord.Color.blue()
            )

            final_char_layout.add_field(name = "Faction", value = faction, inline = False)
            final_char_layout.add_field(name = "Job", value = job, inline = True)
            final_char_layout.add_field(name = "Legion", value = legion, inline = False)
            final_char_layout.add_field(name = "Weapon", value = weapon_choice, inline = True)
            final_char_layout.add_field(name = "Armor", value = armor, inline = False)
            final_char_layout.add_field(name = "Items", value = items, inline = False)
            final_char_layout.add_field(name = "Ships", value = "None", inline = False)
            final_char_layout.add_field(name = "Money", value = money, inline = True)
            final_char_layout.add_field(name = "Species", value = species, inline = True)
            final_char_layout.set_footer(icon_url = user.avatar_url, text = "React with '✅' if you are content with your character or '❌' to cancel. You have 60 seconds to respond")

            final_char_message = await ctx.send(embed = final_char_layout)

            await final_char_message.add_reaction("✅")
            await final_char_message.add_reaction("❌")

            try:
                reaction, reactor = await client.wait_for('reaction_add', check = reaction_check, timeout = 60)
                go_ahead = str(reaction.emoji)
            except:
                await ctx.send(embed = ran_out_of_time_em)
                return
            
            if go_ahead == "❌":
                await ctx.send(embed = cancelled_em)
                return
            
            if str(reaction.emoji) not in ["✅","❌"]:
                await ctx.send(embed = invalid_reaction_em)
                return
            
            if True:
                if str(user.id) in users:
                    users[str(user.id)][character_name] = {}
                    users[str(user.id)][character_name]["faction"] = faction
                    users[str(user.id)][character_name]["job"] = job
                    users[str(user.id)][character_name]["legion"] = legion
                    users[str(user.id)][character_name]["weapons"] = weapon_choice
                    users[str(user.id)][character_name]["armor"] = armor
                    users[str(user.id)][character_name]["items"] = items 
                    users[str(user.id)][character_name]["species"] = species
                    users[str(user.id)][character_name]["money"] = 0
                    users[str(user.id)][character_name]["roles"] = roles
                    users[str(user.id)][character_name]["is_character"] = is_character
                    users[str(user.id)][character_name]["ships"] = ships
                    users[str(user.id)][character_name]["units"] = []
                else:
                    users[str(user.id)] = {}
                    users[str(user.id)][character_name] = {}
                    users[str(user.id)][character_name]["faction"] = faction
                    users[str(user.id)][character_name]["job"] = job
                    users[str(user.id)][character_name]["legion"] = legion
                    users[str(user.id)][character_name]["weapons"] = weapon_choice
                    users[str(user.id)][character_name]["armor"] = armor
                    users[str(user.id)][character_name]["items"] = items 
                    users[str(user.id)][character_name]["species"] = species
                    users[str(user.id)][character_name]["money"] = 0
                    users[str(user.id)][character_name]["roles"] = roles
                    users[str(user.id)][character_name]["is_character"] = is_character
                    users[str(user.id)][character_name]["ships"] = ships
                    users[str(user.id)][character_name]["units"] = []

            with open("users.json", "w") as f:
                json.dump(users,f,sort_keys=True, indent=4, separators=(',', ': '))
            
            if str(user.id) not in userids["userids"]:
                userids["userids"].append(str(user.id))
                with open("userids.json", "w") as f:
                    json.dump(userids,f,sort_keys=True, indent=4, separators=(',', ': '))
            
            data_success = discord.Embed(
                title = "Data Created Successfully!",
                color = discord.Color.green()
            )
            await ctx.send(embed = data_success)
            return
        
        elif faction_choice2 == "🟨":
            species_choice_em = discord.Embed(
                title = "What is your character's species",
                color = discord.Color.blue()
            )
            species_choice_em.add_field(name = "Human - 🟦", value = "** **", inline = False)
            species_choice_em.add_field(name = "Wookie - 🟥", value = "** **", inline = False)
            species_choice_em.add_field(name = "Twi'Lek - 🟧", value = "** **", inline = False)
            species_choice_em.add_field(name = "Rodian - 🟨", value = "** **", inline = False)
            species_choice_em.add_field(name = "Trandoshan - 🟫", value = "** **", inline = False)
            species_choice_em.add_field(name = "Zabrak - 🟪", value = "** **", inline = False)
            species_choice_em.add_field(name = "Chiss - ⬜", value = "** **", inline = False)
            species_choice_em.add_field(name = "Cancel - ❌", value = "** **", inline = False)
            species_choice_em.set_footer(text = "You have 5 minutes to respond")
            species_choice_em.set_thumbnail(
                url = "https://static.wikia.nocookie.net/theclonewiki/images/c/c8/Garnac-SWE.png/revision/latest/top-crop/width/360/height/360?cb=20200814083509"
                )

            species_choice_msg = await ctx.send(embed = species_choice_em)
            await species_choice_msg.add_reaction("🟦")
            await species_choice_msg.add_reaction("🟥")
            await species_choice_msg.add_reaction("🟧")
            await species_choice_msg.add_reaction("🟨")
            await species_choice_msg.add_reaction("🟫")
            await species_choice_msg.add_reaction("🟪")
            await species_choice_msg.add_reaction("⬜")
            await species_choice_msg.add_reaction("❌")
            
            species = {
                "🟦" : "Human",
                "🟥" : "Wookie",
                "🟧" : "Twi'Lek",
                "🟨" : "Rodian",
                "🟫" : "Trandoshan",
                "🟪" : "Zabrak",
                "⬜" : "Chiss"
            }

            try:
                reaction, reactor = await client.wait_for('reaction_add', check = reaction_check, timeout = 60)
                species_choice = str(reaction.emoji)
            except:
                await ctx.send(embed = ran_out_of_time_em)
                return
            
            if species_choice not in ["🟦","🟥","🟧","🟨","🟫","🟪","⬜","❌"]:
                await ctx.send(embed = invalid_reaction_em)
                return 


            if species_choice == "❌":
                await ctx.send(embed = cancelled_em)
                return

            elif species_choice == "🟦":
                character_name_em = discord.Embed(
                    title = "What is the name of your HUMAN character?",
                    color = discord.Color.blue()
                )
                character_name_em.add_field(
                    name = "Separatist Organic Human Soldier Format:", 
                    value = "Examples: Zaphod Beeblebrox, Rogmi Aschansa, Hugh Monnrider, etc.",
                    inline = False
                    )
                character_name_em.description = "Human Name Generator [Click Here](https://www.dimfuture.net/starwars/random/generate.php)"
                character_name_em.set_thumbnail(
                    url = "https://www.seekpng.com/png/full/396-3964474_corsec-investigator-sof-star-wars-rpg-human.png"
                )

            elif species_choice == "🟥":
                character_name_em = discord.Embed(
                    title = "What is the name of your WOOKIE character?",
                    color = discord.Color.blue()
                )
                character_name_em.add_field(
                    name = "Separatist Organic Wookie Soldier Format:", 
                    value = "Examples: Wrhokyyyrk, Gwewbyigglun, Ladivgerrfarl, etc.",
                    inline = False
                    )
                character_name_em.description = "Wookie Name Generator [Click Here](https://www.fantasynamegenerators.com/sw-wookiee-names.php)"
                character_name_em.set_thumbnail(
                    url = "https://img.pngio.com/star-wars-png-images-transparent-free-download-pngmartcom-wookie-png-1249_2139.png"
                )
            
            elif species_choice == "🟧":
                character_name_em = discord.Embed(
                    title = "What is the name of your TWI'LEK character?",
                    color = discord.Color.blue()
                )
                character_name_em.add_field(
                    name = "Separatist Organic Twi-Lek Soldier Format:", 
                    value = "Examples: Oulom'crotew, Oefepvuwem, Atad'tosu, etc.",
                    inline = False
                    )
                character_name_em.description = "Twi'Lek Name Generator [Click Here](https://www.fantasynamegenerators.com/twilek-names.php)"
                character_name_em.set_thumbnail(
                    url = "https://www.pngkit.com/png/detail/197-1972208_cham-syndulla-male-twi-lek.png"
                )

            elif species_choice == "🟨":
                character_name_em = discord.Embed(
                    title = "What is the name of your RODIAN character?",
                    color = discord.Color.blue()
                )
                character_name_em.add_field(
                    name = "Separatist Organic Rodian Soldier Format:", 
                    value = "Examples: Twall Brossull, Dweybedra Jurn, Droin Sangi, etc.",
                    inline = False
                    )
                character_name_em.description = "Rodian Name Generator [Click Here](https://www.fantasynamegenerators.com/sw-rodian-names.php)"
                character_name_em.set_thumbnail(
                    url = "https://pm1.narvii.com/6174/4e0ad22475791a1395ade8034b37177514998379_00.jpg"
                )
            
            elif species_choice == "🟫":
                character_name_em = discord.Embed(
                    title = "What is the name of your TRANDOSHAN character?",
                    color = discord.Color.blue()
                )
                character_name_em.add_field(
                    name = "Separatist Organic Trandoshan Soldier Format:", 
                    value = "Examples: Kik Klers, Britloomx Keet, Sskob Klaabut, etc.",
                    inline = False
                    )
                character_name_em.description = "Rodian Name Generator [Click Here](https://www.fantasynamegenerators.com/sw-trandoshan-names.php)"
                character_name_em.set_thumbnail(
                    url = "https://i.pinimg.com/originals/8b/4a/e5/8b4ae5301f3e884badab421c8b6e13b7.jpg"
                )
            
            elif species_choice == "🟪":
                character_name_em = discord.Embed(
                    title = "What is the name of your ZABRAK character?",
                    color = discord.Color.blue()
                )
                character_name_em.add_field(
                    name = "Separatist Organic Zabrak Soldier Format:", 
                    value = "Examples: Stukruto, Bluruu, Vrogrop, etc.",
                    inline = False
                    )
                character_name_em.description = "Zabrak Name Generator [Click Here](https://www.fantasynamegenerators.com/zabrak-names.php)"
                character_name_em.set_thumbnail(
                    url = "https://static.wikia.nocookie.net/starwars/images/3/3f/MiraZabrak.jpg/revision/latest?cb=20180808211843"
                )
            
            elif species_choice == "⬜":
                character_name_em = discord.Embed(
                    title = "What is the name of your CHISS character?",
                    color = discord.Color.blue()
                )
                character_name_em.add_field(
                    name = "Separatist Organic Chiss Soldier Format:", 
                    value = "Examples: Sremi'poatha'krurtirre, Weth'iceal'beso, Vaw'viaw'hairkau, etc.",
                    inline = False
                    )
                character_name_em.description = "Chiss Name Generator [Click Here](https://www.fantasynamegenerators.com/chiss-names.php)"
                character_name_em.set_thumbnail(
                    url = "https://static.wikia.nocookie.net/starwars/images/b/b2/Aralani-full.png/revision/latest?cb=20190716134722"
                )


            character_name_em.set_footer(
                text = "You have 5 minutes to respond. Send cancel to cancel"
                )

            await ctx.send(embed = character_name_em)

            try:
                character_name = str((await client.wait_for('message', check=message_check, timeout=300)).content)
            except:
                await ctx.send(embed = ran_out_of_time_em)
                return
            
            if character_name.lower() == "cancel":
                await ctx.send(embed = cancelled_em)
                return
            
            for id in userids["userids"]:
                for chars in users[id]:
                    if character_name.lower() == chars.lower():
                        duplicate_name_em = discord.Embed(
                            title = "Duplicate name detected!",
                            color = discord.Color.red()
                        )
                        duplicate_name_em.add_field(name = f"Your name is identical to {chars}", value = f"That pre-existing character belongs to <@{id}>")
                        duplicate_name_em.set_footer(text = "Command reset")
                        await ctx.send(embed = duplicate_name_em)
                        return
            
            
            faction = faction_dict1[faction_choice1]
            job = separatistDict[faction_choice2]
            legion = "None"
            weapon_choice = None
            armor = "None"
            items = []
            roles = [faction,job]
            species = species[species_choice]
            money = 2000000
            is_character = "no"
            ships = []

            final_char_layout = discord.Embed(
                title = f"This is your Character: {character_name}",
                color = discord.Color.blue()
            )

            final_char_layout.add_field(name = "Faction", value = faction, inline = False)
            final_char_layout.add_field(name = "Job", value = job, inline = True)
            final_char_layout.add_field(name = "Legion", value = legion, inline = False)
            final_char_layout.add_field(name = "Weapon", value = "None", inline = True)
            final_char_layout.add_field(name = "Armor", value = armor, inline = False)
            final_char_layout.add_field(name = "Items", value = "None", inline = False)
            final_char_layout.add_field(name = "Ships", value = "None", inline = False)
            final_char_layout.add_field(name = "Money", value = money, inline = True)
            final_char_layout.add_field(name = "Species", value = species, inline = True)
            final_char_layout.set_footer(icon_url = user.avatar_url, text = "React with '✅' if you are content with your character or '❌' to cancel. You have 60 seconds to respond")

            final_char_message = await ctx.send(embed = final_char_layout)

            await final_char_message.add_reaction("✅")
            await final_char_message.add_reaction("❌")

            try:
                reaction, reactor = await client.wait_for('reaction_add', check = reaction_check, timeout = 60)
                go_ahead = str(reaction.emoji)
            except:
                await ctx.send(embed = ran_out_of_time_em)
                return
            
            if go_ahead == "❌":
                await ctx.send(embed = cancelled_em)
                return
            
            if str(reaction.emoji) not in ["✅","❌"]:
                await ctx.send(embed = invalid_reaction_em)
                return
            
            if True:
                if str(user.id) in users:
                    users[str(user.id)][character_name] = {}
                    users[str(user.id)][character_name]["faction"] = faction
                    users[str(user.id)][character_name]["job"] = job
                    users[str(user.id)][character_name]["legion"] = legion
                    users[str(user.id)][character_name]["weapons"] = []
                    users[str(user.id)][character_name]["armor"] = armor
                    users[str(user.id)][character_name]["items"] = items 
                    users[str(user.id)][character_name]["species"] = species
                    users[str(user.id)][character_name]["money"] = money 
                    users[str(user.id)][character_name]["roles"] = roles
                    users[str(user.id)][character_name]["is_character"] = is_character
                    users[str(user.id)][character_name]["ships"] = ships
                    users[str(user.id)][character_name]["units"] = []
                else:
                    users[str(user.id)] = {}
                    users[str(user.id)][character_name] = {}
                    users[str(user.id)][character_name]["faction"] = faction
                    users[str(user.id)][character_name]["job"] = job
                    users[str(user.id)][character_name]["legion"] = legion
                    users[str(user.id)][character_name]["weapons"] = []
                    users[str(user.id)][character_name]["armor"] = armor
                    users[str(user.id)][character_name]["items"] = items 
                    users[str(user.id)][character_name]["species"] = species
                    users[str(user.id)][character_name]["money"] = 0
                    users[str(user.id)][character_name]["roles"] = roles
                    users[str(user.id)][character_name]["is_character"] = is_character
                    users[str(user.id)][character_name]["ships"] = ships
                    users[str(user.id)][character_name]["units"] = []

            with open("users.json", "w") as f:
                json.dump(users,f,sort_keys=True, indent=4, separators=(',', ': '))
            
            if str(user.id) not in userids["userids"]:
                userids["userids"].append(str(user.id))
                with open("userids.json", "w") as f:
                    json.dump(userids,f,sort_keys=True, indent=4, separators=(',', ': '))
            
            data_success = discord.Embed(
                title = "Data Created Successfully!",
                color = discord.Color.green()
            )
            await ctx.send(embed = data_success)
            return

        elif faction_choice2 == "🟫":
                species_choice_em = discord.Embed(
                    title = "What is your character's species",
                    color = discord.Color.blue()
                )
                species_choice_em.add_field(name = "Human - 🟦", value = "** **", inline = False)
                species_choice_em.add_field(name = "Wookie - 🟥", value = "** **", inline = False)
                species_choice_em.add_field(name = "Twi'Lek - 🟧", value = "** **", inline = False)
                species_choice_em.add_field(name = "Rodian - 🟨", value = "** **", inline = False)
                species_choice_em.add_field(name = "Trandoshan - 🟫", value = "** **", inline = False)
                species_choice_em.add_field(name = "Zabrak - 🟪", value = "** **", inline = False)
                species_choice_em.add_field(name = "Chiss - ⬜", value = "** **", inline = False)
                species_choice_em.add_field(name = "Cancel - ❌", value = "** **", inline = False)
                species_choice_em.set_footer(text = "You have 5 minutes to respond")
                species_choice_em.set_thumbnail(
                    url = "https://static.wikia.nocookie.net/theclonewiki/images/c/c8/Garnac-SWE.png/revision/latest/top-crop/width/360/height/360?cb=20200814083509"
                    )

                species_choice_msg = await ctx.send(embed = species_choice_em)
                await species_choice_msg.add_reaction("🟦")
                await species_choice_msg.add_reaction("🟥")
                await species_choice_msg.add_reaction("🟧")
                await species_choice_msg.add_reaction("🟨")
                await species_choice_msg.add_reaction("🟫")
                await species_choice_msg.add_reaction("🟪")
                await species_choice_msg.add_reaction("⬜")
                await species_choice_msg.add_reaction("❌")
                
                species = {
                    "🟦" : "Human",
                    "🟥" : "Wookie",
                    "🟧" : "Twi'Lek",
                    "🟨" : "Rodian",
                    "🟫" : "Trandoshan",
                    "🟪" : "Zabrak",
                    "⬜" : "Chiss"
                }

                try:
                    reaction, reactor = await client.wait_for('reaction_add', check = reaction_check, timeout = 60)
                    species_choice = str(reaction.emoji)
                except:
                    await ctx.send(embed = ran_out_of_time_em)
                    return
                
                if species_choice not in ["🟦","🟥","🟧","🟨","🟫","🟪","⬜","❌"]:
                    await ctx.send(embed = invalid_reaction_em)
                    return 


                if species_choice == "❌":
                    await ctx.send(embed = cancelled_em)
                    return

                elif species_choice == "🟦":
                    character_name_em = discord.Embed(
                        title = "What is the name of your HUMAN character?",
                        color = discord.Color.blue()
                    )
                    character_name_em.add_field(
                        name = "Separatist Organic Human Format:", 
                        value = "Examples: Zaphod Beeblebrox, Rogmi Aschansa, Hugh Monnrider, etc.",
                        inline = False
                        )
                    character_name_em.description = "Human Name Generator [Click Here](https://www.dimfuture.net/starwars/random/generate.php)"
                    character_name_em.set_thumbnail(
                        url = "https://www.seekpng.com/png/full/396-3964474_corsec-investigator-sof-star-wars-rpg-human.png"
                    )

                elif species_choice == "🟥":
                    character_name_em = discord.Embed(
                        title = "What is the name of your WOOKIE character?",
                        color = discord.Color.blue()
                    )
                    character_name_em.add_field(
                        name = "Separatist Organic Wookie Navy Ensign Format:", 
                        value = "Examples: Wrhokyyyrk, Gwewbyigglun, Ladivgerrfarl, etc.",
                        inline = False
                        )
                    character_name_em.description = "Wookie Name Generator [Click Here](https://www.fantasynamegenerators.com/sw-wookiee-names.php)"
                    character_name_em.set_thumbnail(
                        url = "https://img.pngio.com/star-wars-png-images-transparent-free-download-pngmartcom-wookie-png-1249_2139.png"
                    )
                
                elif species_choice == "🟧":
                    character_name_em = discord.Embed(
                        title = "What is the name of your TWI'LEK character?",
                        color = discord.Color.blue()
                    )
                    character_name_em.add_field(
                        name = "Separatist Organic Twi-Lek Navy Ensign Format:", 
                        value = "Examples: Oulom'crotew, Oefepvuwem, Atad'tosu, etc.",
                        inline = False
                        )
                    character_name_em.description = "Twi'Lek Name Generator [Click Here](https://www.fantasynamegenerators.com/twilek-names.php)"
                    character_name_em.set_thumbnail(
                        url = "https://www.pngkit.com/png/detail/197-1972208_cham-syndulla-male-twi-lek.png"
                    )

                elif species_choice == "🟨":
                    character_name_em = discord.Embed(
                        title = "What is the name of your RODIAN character?",
                        color = discord.Color.blue()
                    )
                    character_name_em.add_field(
                        name = "Separatist Organic Rodian Navy Ensign Format:", 
                        value = "Examples: Twall Brossull, Dweybedra Jurn, Droin Sangi, etc.",
                        inline = False
                        )
                    character_name_em.description = "Rodian Name Generator [Click Here](https://www.fantasynamegenerators.com/sw-rodian-names.php)"
                    character_name_em.set_thumbnail(
                        url = "https://pm1.narvii.com/6174/4e0ad22475791a1395ade8034b37177514998379_00.jpg"
                    )
                
                elif species_choice == "🟫":
                    character_name_em = discord.Embed(
                        title = "What is the name of your TRANDOSHAN character?",
                        color = discord.Color.blue()
                    )
                    character_name_em.add_field(
                        name = "Separatist Organic Trandoshan Navy Ensign Format:", 
                        value = "Examples: Kik Klers, Britloomx Keet, Sskob Klaabut, etc.",
                        inline = False
                        )
                    character_name_em.description = "Rodian Name Generator [Click Here](https://www.fantasynamegenerators.com/sw-trandoshan-names.php)"
                    character_name_em.set_thumbnail(
                        url = "https://i.pinimg.com/originals/8b/4a/e5/8b4ae5301f3e884badab421c8b6e13b7.jpg"
                    )
                
                elif species_choice == "🟪":
                    character_name_em = discord.Embed(
                        title = "What is the name of your ZABRAK character?",
                        color = discord.Color.blue()
                    )
                    character_name_em.add_field(
                        name = "Separatist Organic Zabrak Navy Ensign Format:", 
                        value = "Examples: Stukruto, Bluruu, Vrogrop, etc.",
                        inline = False
                        )
                    character_name_em.description = "Zabrak Name Generator [Click Here](https://www.fantasynamegenerators.com/zabrak-names.php)"
                    character_name_em.set_thumbnail(
                        url = "https://static.wikia.nocookie.net/starwars/images/3/3f/MiraZabrak.jpg/revision/latest?cb=20180808211843"
                    )
                
                elif species_choice == "⬜":
                    character_name_em = discord.Embed(
                        title = "What is the name of your Chiss Navy Ensign character?",
                        color = discord.Color.blue()
                    )
                    character_name_em.add_field(
                        name = "Separatist Organic Chiss Navy Ensign Format:", 
                        value = "Examples: Sremi'poatha'krurtirre, Weth'iceal'beso, Vaw'viaw'hairkau, etc.",
                        inline = False
                        )
                    character_name_em.description = "Chiss Name Generator [Click Here](https://www.fantasynamegenerators.com/chiss-names.php)"
                    character_name_em.set_thumbnail(
                        url = "https://static.wikia.nocookie.net/starwars/images/b/b2/Aralani-full.png/revision/latest?cb=20190716134722"
                    )


                character_name_em.set_footer(
                    text = "You have 5 minutes to respond. Send cancel to cancel"
                    )

                await ctx.send(embed = character_name_em)

                try:
                    character_name = str((await client.wait_for('message', check=message_check, timeout=300)).content)
                except:
                    await ctx.send(embed = ran_out_of_time_em)
                    return
                
                if character_name.lower() == "cancel":
                    await ctx.send(embed = cancelled_em)
                    return
                
                for id in userids["userids"]:
                    for chars in users[id]:
                        if character_name.lower() == chars.lower():
                            duplicate_name_em = discord.Embed(
                                title = "Duplicate name detected!",
                                color = discord.Color.red()
                            )
                            duplicate_name_em.add_field(name = f"Your name is identical to {chars}", value = f"That pre-existing character belongs to <@{id}>")
                            duplicate_name_em.set_footer(text = "Command reset")
                            await ctx.send(embed = duplicate_name_em)
                            return
                
                
                faction = faction_dict1[faction_choice1]
                job = separatistDict[faction_choice2]
                legion = "None"
                weapon_choice = ["SE-14"]
                armor = "None"
                items = ["Datapad","Comms"]
                roles = [faction,job]
                species = species[species_choice]
                money = 0
                is_character = "no"
                ships = []

                final_char_layout = discord.Embed(
                    title = f"This is your Character: {character_name}",
                    color = discord.Color.blue()
                )

                final_char_layout.add_field(name = "Faction", value = faction, inline = False)
                final_char_layout.add_field(name = "Job", value = job, inline = True)
                final_char_layout.add_field(name = "Legion", value = legion, inline = False)
                final_char_layout.add_field(name = "Weapon", value = weapon_choice, inline = True)
                final_char_layout.add_field(name = "Armor", value = armor, inline = False)
                final_char_layout.add_field(name = "Items", value = items, inline = False)
                final_char_layout.add_field(name = "Ships", value = "None", inline = False)
                final_char_layout.add_field(name = "Money", value = money, inline = True)
                final_char_layout.add_field(name = "Species", value = species, inline = True)
                final_char_layout.set_footer(icon_url = user.avatar_url, text = "React with '✅' if you are content with your character or '❌' to cancel. You have 60 seconds to respond")

                final_char_message = await ctx.send(embed = final_char_layout)

                await final_char_message.add_reaction("✅")
                await final_char_message.add_reaction("❌")

                try:
                    reaction, reactor = await client.wait_for('reaction_add', check = reaction_check, timeout = 60)
                    go_ahead = str(reaction.emoji)
                except:
                    await ctx.send(embed = ran_out_of_time_em)
                    return
                
                if go_ahead == "❌":
                    await ctx.send(embed = cancelled_em)
                    return
                
                if str(reaction.emoji) not in ["✅","❌"]:
                    await ctx.send(embed = invalid_reaction_em)
                    return
                
                if True:
                    if str(user.id) in users:
                        users[str(user.id)][character_name] = {}
                        users[str(user.id)][character_name]["faction"] = faction
                        users[str(user.id)][character_name]["job"] = job
                        users[str(user.id)][character_name]["legion"] = legion
                        users[str(user.id)][character_name]["weapons"] = weapon_choice
                        users[str(user.id)][character_name]["armor"] = armor
                        users[str(user.id)][character_name]["items"] = items 
                        users[str(user.id)][character_name]["species"] = species
                        users[str(user.id)][character_name]["money"] = money 
                        users[str(user.id)][character_name]["roles"] = roles
                        users[str(user.id)][character_name]["is_character"] = is_character
                        users[str(user.id)][character_name]["ships"] = ships
                        users[str(user.id)][character_name]["units"] = []
                    else:
                        users[str(user.id)] = {}
                        users[str(user.id)][character_name] = {}
                        users[str(user.id)][character_name]["faction"] = faction
                        users[str(user.id)][character_name]["job"] = job
                        users[str(user.id)][character_name]["legion"] = legion
                        users[str(user.id)][character_name]["weapons"] = weapon_choice
                        users[str(user.id)][character_name]["armor"] = armor
                        users[str(user.id)][character_name]["items"] = items 
                        users[str(user.id)][character_name]["species"] = species
                        users[str(user.id)][character_name]["money"] = 0
                        users[str(user.id)][character_name]["roles"] = roles
                        users[str(user.id)][character_name]["is_character"] = is_character
                        users[str(user.id)][character_name]["ships"] = ships
                        users[str(user.id)][character_name]["units"] = []

                with open("users.json", "w") as f:
                    json.dump(users,f,sort_keys=True, indent=4, separators=(',', ': '))
                
                if str(user.id) not in userids["userids"]:
                    userids["userids"].append(str(user.id))
                    with open("userids.json", "w") as f:
                        json.dump(userids,f,sort_keys=True, indent=4, separators=(',', ': '))
                
                data_success = discord.Embed(
                    title = "Data Created Successfully!",
                    color = discord.Color.green()
                )
                await ctx.send(embed = data_success)
                return

    elif faction_choice1 == "🟧":
                species_choice_em = discord.Embed(
                    title = "What is your character's species",
                    color = discord.Color.blue()
                )
                species_choice_em.add_field(name = "Human - 🟦", value = "** **", inline = False)
                species_choice_em.add_field(name = "Wookie - 🟥", value = "** **", inline = False)
                species_choice_em.add_field(name = "Twi'Lek - 🟧", value = "** **", inline = False)
                species_choice_em.add_field(name = "Rodian - 🟨", value = "** **", inline = False)
                species_choice_em.add_field(name = "Trandoshan - 🟫", value = "** **", inline = False)
                species_choice_em.add_field(name = "Zabrak - 🟪", value = "** **", inline = False)
                species_choice_em.add_field(name = "Chiss - ⬜", value = "** **", inline = False)
                species_choice_em.add_field(name = "Mandalorian - 🟩", value = "** **", inline = False)
                species_choice_em.add_field(name = "Cancel - ❌", value = "** **", inline = False)
                species_choice_em.set_footer(text = "You have 5 minutes to respond")
                species_choice_em.set_thumbnail(
                    url = "https://static.wikia.nocookie.net/theclonewiki/images/c/c8/Garnac-SWE.png/revision/latest/top-crop/width/360/height/360?cb=20200814083509"
                    )

                species_choice_msg = await ctx.send(embed = species_choice_em)
                await species_choice_msg.add_reaction("🟦")
                await species_choice_msg.add_reaction("🟥")
                await species_choice_msg.add_reaction("🟧")
                await species_choice_msg.add_reaction("🟨")
                await species_choice_msg.add_reaction("🟫")
                await species_choice_msg.add_reaction("🟪")
                await species_choice_msg.add_reaction("⬜")
                await species_choice_msg.add_reaction("🟩")
                await species_choice_msg.add_reaction("❌")
                
                species = {
                    "🟦" : "Human",
                    "🟥" : "Wookie",
                    "🟧" : "Twi'Lek",
                    "🟨" : "Rodian",
                    "🟫" : "Trandoshan",
                    "🟪" : "Zabrak",
                    "⬜" : "Chiss",
                    "🟩" : "Mandalorian"
                }

                try:
                    reaction, reactor = await client.wait_for('reaction_add', check = reaction_check, timeout = 60)
                    species_choice = str(reaction.emoji)
                except:
                    await ctx.send(embed = ran_out_of_time_em)
                    return
                
                if species_choice not in ["🟦","🟥","🟧","🟨","🟫","🟪","⬜","🟩","❌"]:
                    await ctx.send(embed = invalid_reaction_em)
                    return 


                if species_choice == "❌":
                    await ctx.send(embed = cancelled_em)
                    return

                elif species_choice == "🟦":
                    character_name_em = discord.Embed(
                        title = "What is the name of your HUMAN character?",
                        color = discord.Color.blue()
                    )
                    character_name_em.add_field(
                        name = "Human Bounty Hunter Format:", 
                        value = "Examples: Zaphod Beeblebrox, Rogmi Aschansa, Hugh Monnrider, etc.",
                        inline = False
                        )
                    character_name_em.description = "Human Name Generator [Click Here](https://www.dimfuture.net/starwars/random/generate.php)"
                    character_name_em.set_thumbnail(
                        url = "https://www.seekpng.com/png/full/396-3964474_corsec-investigator-sof-star-wars-rpg-human.png"
                    )

                elif species_choice == "🟥":
                    character_name_em = discord.Embed(
                        title = "What is the name of your WOOKIE character?",
                        color = discord.Color.blue()
                    )
                    character_name_em.add_field(
                        name = "Wookie Bounty Hunter Format:", 
                        value = "Examples: Wrhokyyyrk, Gwewbyigglun, Ladivgerrfarl, etc.",
                        inline = False
                        )
                    character_name_em.description = "Wookie Name Generator [Click Here](https://www.fantasynamegenerators.com/sw-wookiee-names.php)"
                    character_name_em.set_thumbnail(
                        url = "https://img.pngio.com/star-wars-png-images-transparent-free-download-pngmartcom-wookie-png-1249_2139.png"
                    )
                
                elif species_choice == "🟧":
                    character_name_em = discord.Embed(
                        title = "What is the name of your TWI'LEK character?",
                        color = discord.Color.blue()
                    )
                    character_name_em.add_field(
                        name = "Twi'Lek Bounty Hunter Format:", 
                        value = "Examples: Oulom'crotew, Oefepvuwem, Atad'tosu, etc.",
                        inline = False
                        )
                    character_name_em.description = "Twi'Lek Name Generator [Click Here](https://www.fantasynamegenerators.com/twilek-names.php)"
                    character_name_em.set_thumbnail(
                        url = "https://www.pngkit.com/png/detail/197-1972208_cham-syndulla-male-twi-lek.png"
                    )

                elif species_choice == "🟨":
                    character_name_em = discord.Embed(
                        title = "What is the name of your RODIAN character?",
                        color = discord.Color.blue()
                    )
                    character_name_em.add_field(
                        name = "Rodian Bounty Hunter Format:", 
                        value = "Examples: Twall Brossull, Dweybedra Jurn, Droin Sangi, etc.",
                        inline = False
                        )
                    character_name_em.description = "Rodian Name Generator [Click Here](https://www.fantasynamegenerators.com/sw-rodian-names.php)"
                    character_name_em.set_thumbnail(
                        url = "https://pm1.narvii.com/6174/4e0ad22475791a1395ade8034b37177514998379_00.jpg"
                    )
                
                elif species_choice == "🟫":
                    character_name_em = discord.Embed(
                        title = "What is the name of your TRANDOSHAN character?",
                        color = discord.Color.blue()
                    )
                    character_name_em.add_field(
                        name = "Trandoshan Bounty Hunter Format:", 
                        value = "Examples: Kik Klers, Britloomx Keet, Sskob Klaabut, etc.",
                        inline = False
                        )
                    character_name_em.description = "Rodian Name Generator [Click Here](https://www.fantasynamegenerators.com/sw-trandoshan-names.php)"
                    character_name_em.set_thumbnail(
                        url = "https://i.pinimg.com/originals/8b/4a/e5/8b4ae5301f3e884badab421c8b6e13b7.jpg"
                    )
                
                elif species_choice == "🟪":
                    character_name_em = discord.Embed(
                        title = "What is the name of your ZABRAK character?",
                        color = discord.Color.blue()
                    )
                    character_name_em.add_field(
                        name = "Zabrak Bounty Hunter Format:", 
                        value = "Examples: Stukruto, Bluruu, Vrogrop, etc.",
                        inline = False
                        )
                    character_name_em.description = "Zabrak Name Generator [Click Here](https://www.fantasynamegenerators.com/zabrak-names.php)"
                    character_name_em.set_thumbnail(
                        url = "https://static.wikia.nocookie.net/starwars/images/3/3f/MiraZabrak.jpg/revision/latest?cb=20180808211843"
                    )
                
                elif species_choice == "⬜":
                    character_name_em = discord.Embed(
                        title = "What is the name of your CHISS character?",
                        color = discord.Color.blue()
                    )
                    character_name_em.add_field(
                        name = "Chiss Bounty Hunter Format:", 
                        value = "Examples: Sremi'poatha'krurtirre, Weth'iceal'beso, Vaw'viaw'hairkau, etc.",
                        inline = False
                        )
                    character_name_em.description = "Chiss Name Generator [Click Here](https://www.fantasynamegenerators.com/chiss-names.php)"
                    character_name_em.set_thumbnail(
                        url = "https://static.wikia.nocookie.net/starwars/images/b/b2/Aralani-full.png/revision/latest?cb=20190716134722"
                    )
                
                elif species_choice == "🟩":
                    character_name_em = discord.Embed(
                        title = "What is the name of your MANDALORIAN character?",
                        color = discord.Color.blue()
                    )
                    character_name_em.add_field(
                        name = "Mandalorian Bounty Hunter Format:", 
                        value = "Examples: Channaeth Shuuss, Cank Agryg, Xujix Rutt, etc.",
                        inline = False
                        )
                    character_name_em.description = "Mandalorian Name Generator [Click Here](https://www.dimfuture.net/starwars/random/generate.php)"
                    character_name_em.set_thumbnail(
                        url = "https://lumiere-a.akamaihd.net/v1/images/image_3104fc48.jpeg?region=246%2C0%2C1170%2C878&width=960"
                    )


                character_name_em.set_footer(
                    text = "You have 5 minutes to respond. Send cancel to cancel"
                    )

                await ctx.send(embed = character_name_em)

                try:
                    character_name = str((await client.wait_for('message', check=message_check, timeout=300)).content)
                except:
                    await ctx.send(embed = ran_out_of_time_em)
                    return
                
                if character_name.lower() == "cancel":
                    await ctx.send(embed = cancelled_em)
                    return
                
                for id in userids["userids"]:
                    for chars in users[id]:
                        if character_name.lower() == chars.lower():
                            duplicate_name_em = discord.Embed(
                                title = "Duplicate name detected!",
                                color = discord.Color.red()
                            )
                            duplicate_name_em.add_field(name = f"Your name is identical to {chars}", value = f"That pre-existing character belongs to <@{id}>")
                            duplicate_name_em.set_footer(text = "Command reset")
                            await ctx.send(embed = duplicate_name_em)
                            return
                
                
                faction = "Bounty Hunter Guild"
                job = "Bounty Hunter"
                legion = "None"
                weapon_choice = []
                armor = "None"
                items = []
                species = species[species_choice]
                roles = [faction,job,species]
                money = 2000000
                is_character = "no"
                ships = []

                if species_choice == "🟩":
                    armor = "Mandalorian Lightweight Plasteel Armor"


                final_char_layout = discord.Embed(
                    title = f"This is your Character: {character_name}",
                    color = discord.Color.blue()
                )

                final_char_layout.add_field(name = "Faction", value = faction, inline = False)
                final_char_layout.add_field(name = "Job", value = job, inline = True)
                final_char_layout.add_field(name = "Legion", value = legion, inline = False)
                final_char_layout.add_field(name = "Weapon", value = "None", inline = True)
                final_char_layout.add_field(name = "Armor", value = armor, inline = False)
                final_char_layout.add_field(name = "Items", value = "None", inline = False)
                final_char_layout.add_field(name = "Ships", value = "None", inline = False)
                final_char_layout.add_field(name = "Money", value = money, inline = True)
                final_char_layout.add_field(name = "Species", value = species, inline = True)
                final_char_layout.set_footer(icon_url = user.avatar_url, text = "React with '✅' if you are content with your character or '❌' to cancel. You have 60 seconds to respond")

                final_char_message = await ctx.send(embed = final_char_layout)

                await final_char_message.add_reaction("✅")
                await final_char_message.add_reaction("❌")

                try:
                    reaction, reactor = await client.wait_for('reaction_add', check = reaction_check, timeout = 60)
                    go_ahead = str(reaction.emoji)
                except:
                    await ctx.send(embed = ran_out_of_time_em)
                    return
                
                if go_ahead == "❌":
                    await ctx.send(embed = cancelled_em)
                    return
                
                if str(reaction.emoji) not in ["✅","❌"]:
                    await ctx.send(embed = invalid_reaction_em)
                    return
                
                if True:
                    if str(user.id) in users:
                        users[str(user.id)][character_name] = {}
                        users[str(user.id)][character_name]["faction"] = faction
                        users[str(user.id)][character_name]["job"] = job
                        users[str(user.id)][character_name]["legion"] = legion
                        users[str(user.id)][character_name]["weapons"] = weapon_choice
                        users[str(user.id)][character_name]["armor"] = armor
                        users[str(user.id)][character_name]["items"] = items 
                        users[str(user.id)][character_name]["species"] = species
                        users[str(user.id)][character_name]["money"] = money 
                        users[str(user.id)][character_name]["roles"] = roles
                        users[str(user.id)][character_name]["is_character"] = is_character
                        users[str(user.id)][character_name]["ships"] = ships
                        users[str(user.id)][character_name]["units"] = []
                    else:
                        users[str(user.id)] = {}
                        users[str(user.id)][character_name] = {}
                        users[str(user.id)][character_name]["faction"] = faction
                        users[str(user.id)][character_name]["job"] = job
                        users[str(user.id)][character_name]["legion"] = legion
                        users[str(user.id)][character_name]["weapons"] = weapon_choice
                        users[str(user.id)][character_name]["armor"] = armor
                        users[str(user.id)][character_name]["items"] = items 
                        users[str(user.id)][character_name]["species"] = species
                        users[str(user.id)][character_name]["money"] = 0
                        users[str(user.id)][character_name]["roles"] = roles
                        users[str(user.id)][character_name]["is_character"] = is_character
                        users[str(user.id)][character_name]["ships"] = ships
                        users[str(user.id)][character_name]["units"] = []

                with open("users.json", "w") as f:
                    json.dump(users,f,sort_keys=True, indent=4, separators=(',', ': '))
                
                if str(user.id) not in userids["userids"]:
                    userids["userids"].append(str(user.id))
                    with open("userids.json", "w") as f:
                        json.dump(userids,f,sort_keys=True, indent=4, separators=(',', ': '))
                
                data_success = discord.Embed(
                    title = "Data Created Successfully!",
                    color = discord.Color.green()
                )
                await ctx.send(embed = data_success)
                return

    elif faction_choice1 == "🟨":
                species_choice_em = discord.Embed(
                    title = "What is your character's species",
                    color = discord.Color.blue()
                )
                species_choice_em.add_field(name = "Human - 🟦", value = "** **", inline = False)
                species_choice_em.add_field(name = "Wookie - 🟥", value = "** **", inline = False)
                species_choice_em.add_field(name = "Twi'Lek - 🟧", value = "** **", inline = False)
                species_choice_em.add_field(name = "Rodian - 🟨", value = "** **", inline = False)
                species_choice_em.add_field(name = "Trandoshan - 🟫", value = "** **", inline = False)
                species_choice_em.add_field(name = "Zabrak - 🟪", value = "** **", inline = False)
                species_choice_em.add_field(name = "Chiss - ⬜", value = "** **", inline = False)
                species_choice_em.add_field(name = "Mandalorian - 🟩", value = "** **", inline = False)
                species_choice_em.add_field(name = "Cancel - ❌", value = "** **", inline = False)
                species_choice_em.set_footer(text = "You have 5 minutes to respond")
                species_choice_em.set_thumbnail(
                    url = "https://static.wikia.nocookie.net/theclonewiki/images/c/c8/Garnac-SWE.png/revision/latest/top-crop/width/360/height/360?cb=20200814083509"
                    )

                species_choice_msg = await ctx.send(embed = species_choice_em)
                await species_choice_msg.add_reaction("🟦")
                await species_choice_msg.add_reaction("🟥")
                await species_choice_msg.add_reaction("🟧")
                await species_choice_msg.add_reaction("🟨")
                await species_choice_msg.add_reaction("🟫")
                await species_choice_msg.add_reaction("🟪")
                await species_choice_msg.add_reaction("⬜")
                await species_choice_msg.add_reaction("🟩")
                await species_choice_msg.add_reaction("❌")
                
                species = {
                    "🟦" : "Human",
                    "🟥" : "Wookie",
                    "🟧" : "Twi'Lek",
                    "🟨" : "Rodian",
                    "🟫" : "Trandoshan",
                    "🟪" : "Zabrak",
                    "⬜" : "Chiss",
                    "🟩" : "Mandalorian"
                }

                try:
                    reaction, reactor = await client.wait_for('reaction_add', check = reaction_check, timeout = 60)
                    species_choice = str(reaction.emoji)
                except:
                    await ctx.send(embed = ran_out_of_time_em)
                    return
                
                if species_choice not in ["🟦","🟥","🟧","🟨","🟫","🟪","⬜","🟩","❌"]:
                    await ctx.send(embed = invalid_reaction_em)
                    return 


                if species_choice == "❌":
                    await ctx.send(embed = cancelled_em)
                    return

                elif species_choice == "🟦":
                    character_name_em = discord.Embed(
                        title = "What is the name of your HUMAN character?",
                        color = discord.Color.blue()
                    )
                    character_name_em.add_field(
                        name = "Human Smuggler Format:", 
                        value = "Examples: Zaphod Beeblebrox, Rogmi Aschansa, Hugh Monnrider, etc.",
                        inline = False
                        )
                    character_name_em.description = "Human Name Generator [Click Here](https://www.dimfuture.net/starwars/random/generate.php)"
                    character_name_em.set_thumbnail(
                        url = "https://www.seekpng.com/png/full/396-3964474_corsec-investigator-sof-star-wars-rpg-human.png"
                    )

                elif species_choice == "🟥":
                    character_name_em = discord.Embed(
                        title = "What is the name of your WOOKIE character?",
                        color = discord.Color.blue()
                    )
                    character_name_em.add_field(
                        name = "Wookie Smuggler Format:", 
                        value = "Examples: Wrhokyyyrk, Gwewbyigglun, Ladivgerrfarl, etc.",
                        inline = False
                        )
                    character_name_em.description = "Wookie Name Generator [Click Here](https://www.fantasynamegenerators.com/sw-wookiee-names.php)"
                    character_name_em.set_thumbnail(
                        url = "https://img.pngio.com/star-wars-png-images-transparent-free-download-pngmartcom-wookie-png-1249_2139.png"
                    )
                
                elif species_choice == "🟧":
                    character_name_em = discord.Embed(
                        title = "What is the name of your TWI'LEK character?",
                        color = discord.Color.blue()
                    )
                    character_name_em.add_field(
                        name = "Twi'Lek Smuggler Format:", 
                        value = "Examples: Oulom'crotew, Oefepvuwem, Atad'tosu, etc.",
                        inline = False
                        )
                    character_name_em.description = "Twi'Lek Name Generator [Click Here](https://www.fantasynamegenerators.com/twilek-names.php)"
                    character_name_em.set_thumbnail(
                        url = "https://www.pngkit.com/png/detail/197-1972208_cham-syndulla-male-twi-lek.png"
                    )

                elif species_choice == "🟨":
                    character_name_em = discord.Embed(
                        title = "What is the name of your RODIAN character?",
                        color = discord.Color.blue()
                    )
                    character_name_em.add_field(
                        name = "Rodian Smuggler Format:", 
                        value = "Examples: Twall Brossull, Dweybedra Jurn, Droin Sangi, etc.",
                        inline = False
                        )
                    character_name_em.description = "Rodian Name Generator [Click Here](https://www.fantasynamegenerators.com/sw-rodian-names.php)"
                    character_name_em.set_thumbnail(
                        url = "https://pm1.narvii.com/6174/4e0ad22475791a1395ade8034b37177514998379_00.jpg"
                    )
                
                elif species_choice == "🟫":
                    character_name_em = discord.Embed(
                        title = "What is the name of your TRANDOSHAN character?",
                        color = discord.Color.blue()
                    )
                    character_name_em.add_field(
                        name = "Trandoshan Smuggler Format:", 
                        value = "Examples: Kik Klers, Britloomx Keet, Sskob Klaabut, etc.",
                        inline = False
                        )
                    character_name_em.description = "Rodian Name Generator [Click Here](https://www.fantasynamegenerators.com/sw-trandoshan-names.php)"
                    character_name_em.set_thumbnail(
                        url = "https://i.pinimg.com/originals/8b/4a/e5/8b4ae5301f3e884badab421c8b6e13b7.jpg"
                    )
                
                elif species_choice == "🟪":
                    character_name_em = discord.Embed(
                        title = "What is the name of your ZABRAK character?",
                        color = discord.Color.blue()
                    )
                    character_name_em.add_field(
                        name = "Zabrak Smuggler Format:", 
                        value = "Examples: Stukruto, Bluruu, Vrogrop, etc.",
                        inline = False
                        )
                    character_name_em.description = "Zabrak Name Generator [Click Here](https://www.fantasynamegenerators.com/zabrak-names.php)"
                    character_name_em.set_thumbnail(
                        url = "https://static.wikia.nocookie.net/starwars/images/3/3f/MiraZabrak.jpg/revision/latest?cb=20180808211843"
                    )
                
                elif species_choice == "⬜":
                    character_name_em = discord.Embed(
                        title = "What is the name of your CHISS character?",
                        color = discord.Color.blue()
                    )
                    character_name_em.add_field(
                        name = "Chiss Smuggler Format:", 
                        value = "Examples: Sremi'poatha'krurtirre, Weth'iceal'beso, Vaw'viaw'hairkau, etc.",
                        inline = False
                        )
                    character_name_em.description = "Chiss Name Generator [Click Here](https://www.fantasynamegenerators.com/chiss-names.php)"
                    character_name_em.set_thumbnail(
                        url = "https://static.wikia.nocookie.net/starwars/images/b/b2/Aralani-full.png/revision/latest?cb=20190716134722"
                    )
                
                elif species_choice == "🟩":
                    character_name_em = discord.Embed(
                        title = "What is the name of your MANDALORIAN character?",
                        color = discord.Color.blue()
                    )
                    character_name_em.add_field(
                        name = "Mandalorian Smuggler Format:", 
                        value = "Examples: Channaeth Shuuss, Cank Agryg, Xujix Rutt, etc.",
                        inline = False
                        )
                    character_name_em.description = "Mandalorian Name Generator [Click Here](https://www.dimfuture.net/starwars/random/generate.php)"
                    character_name_em.set_thumbnail(
                        url = "https://lumiere-a.akamaihd.net/v1/images/image_3104fc48.jpeg?region=246%2C0%2C1170%2C878&width=960"
                    )


                character_name_em.set_footer(
                    text = "You have 5 minutes to respond. Send cancel to cancel"
                    )

                await ctx.send(embed = character_name_em)

                try:
                    character_name = str((await client.wait_for('message', check=message_check, timeout=300)).content)
                except:
                    await ctx.send(embed = ran_out_of_time_em)
                    return
                
                if character_name.lower() == "cancel":
                    await ctx.send(embed = cancelled_em)
                    return
                
                for id in userids["userids"]:
                    for chars in users[id]:
                        if character_name.lower() == chars.lower():
                            duplicate_name_em = discord.Embed(
                                title = "Duplicate name detected!",
                                color = discord.Color.red()
                            )
                            duplicate_name_em.add_field(name = f"Your name is identical to {chars}", value = f"That pre-existing character belongs to <@{id}>")
                            duplicate_name_em.set_footer(text = "Command reset")
                            await ctx.send(embed = duplicate_name_em)
                            return
                
                
                faction = "Smuggler Guild"
                job = "Smuggler"
                legion = "None"
                weapon_choice = []
                armor = "None"
                items = []
                species = species[species_choice]
                roles = [faction,job,species]
                money = 2000000
                is_character = "no"
                ships = []

                if species_choice == "🟩":
                    armor = "Mandalorian Lightweight Plasteel Armor"


                final_char_layout = discord.Embed(
                    title = f"This is your Character: {character_name}",
                    color = discord.Color.blue()
                )

                final_char_layout.add_field(name = "Faction", value = faction, inline = False)
                final_char_layout.add_field(name = "Job", value = job, inline = True)
                final_char_layout.add_field(name = "Legion", value = legion, inline = False)
                final_char_layout.add_field(name = "Weapon", value = "None", inline = True)
                final_char_layout.add_field(name = "Armor", value = armor, inline = False)
                final_char_layout.add_field(name = "Items", value = "None", inline = False)
                final_char_layout.add_field(name = "Ships", value = "None", inline = False)
                final_char_layout.add_field(name = "Money", value = money, inline = True)
                final_char_layout.add_field(name = "Species", value = species, inline = True)
                final_char_layout.set_footer(icon_url = user.avatar_url, text = "React with '✅' if you are content with your character or '❌' to cancel. You have 60 seconds to respond")

                final_char_message = await ctx.send(embed = final_char_layout)

                await final_char_message.add_reaction("✅")
                await final_char_message.add_reaction("❌")

                try:
                    reaction, reactor = await client.wait_for('reaction_add', check = reaction_check, timeout = 60)
                    go_ahead = str(reaction.emoji)
                except:
                    await ctx.send(embed = ran_out_of_time_em)
                    return
                
                if go_ahead == "❌":
                    await ctx.send(embed = cancelled_em)
                    return
                
                if str(reaction.emoji) not in ["✅","❌"]:
                    await ctx.send(embed = invalid_reaction_em)
                    return
                
                if True:
                    if str(user.id) in users:
                        users[str(user.id)][character_name] = {}
                        users[str(user.id)][character_name]["faction"] = faction
                        users[str(user.id)][character_name]["job"] = job
                        users[str(user.id)][character_name]["legion"] = legion
                        users[str(user.id)][character_name]["weapons"] = weapon_choice
                        users[str(user.id)][character_name]["armor"] = armor
                        users[str(user.id)][character_name]["items"] = items 
                        users[str(user.id)][character_name]["species"] = species
                        users[str(user.id)][character_name]["money"] = money 
                        users[str(user.id)][character_name]["roles"] = roles
                        users[str(user.id)][character_name]["is_character"] = is_character
                        users[str(user.id)][character_name]["ships"] = ships
                        users[str(user.id)][character_name]["units"] = []
                    else:
                        users[str(user.id)] = {}
                        users[str(user.id)][character_name] = {}
                        users[str(user.id)][character_name]["faction"] = faction
                        users[str(user.id)][character_name]["job"] = job
                        users[str(user.id)][character_name]["legion"] = legion
                        users[str(user.id)][character_name]["weapons"] = weapon_choice
                        users[str(user.id)][character_name]["armor"] = armor
                        users[str(user.id)][character_name]["items"] = items 
                        users[str(user.id)][character_name]["species"] = species
                        users[str(user.id)][character_name]["money"] = 0
                        users[str(user.id)][character_name]["roles"] = roles
                        users[str(user.id)][character_name]["is_character"] = is_character
                        users[str(user.id)][character_name]["ships"] = ships
                        users[str(user.id)][character_name]["units"] = []

                with open("users.json", "w") as f:
                    json.dump(users,f,sort_keys=True, indent=4, separators=(',', ': '))
                
                if str(user.id) not in userids["userids"]:
                    userids["userids"].append(str(user.id))
                    with open("userids.json", "w") as f:
                        json.dump(userids,f,sort_keys=True, indent=4, separators=(',', ': '))
                
                data_success = discord.Embed(
                    title = "Data Created Successfully!",
                    color = discord.Color.green()
                )
                await ctx.send(embed = data_success)
                return

    elif faction_choice1 == "🟫":
                job_choice_em = discord.Embed(
                    title = "What is your character's job",
                    color = discord.Color.blue()
                )

                job_choice_em.add_field(name = "Foundling - 🟦", value = "** **", inline = False)
                job_choice_em.add_field(name = "Independent - 🟥", value = "** **", inline = False)
                job_choice_em.add_field(name = "Cancel - ❌", value = "** **")
                job_choice_em.set_footer(text = "You have 5 minutes to respond")
                job_choice_em.set_thumbnail(
                    url = "https://www.nicepng.com/png/detail/162-1629264_tg-traditional-games-search-offset-1440-orange-mandalorian.png"
                )
                job_choice_msg = await ctx.send(embed = job_choice_em)

                await job_choice_msg.add_reaction("🟦")
                await job_choice_msg.add_reaction("🟥")
                
                jobDict = {
                    "🟦" : "Foundling",
                    "🟥" : "Independent"
                }

                try:
                    reaction, reactor = await client.wait_for('reaction_add', check = reaction_check, timeout = 60)
                    job_choice = str(reaction.emoji)
                except:
                    await ctx.send(embed = ran_out_of_time_em)
                    return
                
                if job_choice not in ["🟦","🟥","❌"]:
                    await ctx.send(embed = invalid_reaction_em)
                    return 

                if job_choice == "❌":
                    await ctx.send(embed = cancelled_em)
                    return
                
                job_choice = jobDict[job_choice]
                
                character_name_em = discord.Embed(
                    title = "What is the name of your MANDALORIAN character?",
                    color = discord.Color.blue()
                )
                character_name_em.add_field(
                    name = "Mandalorian Smuggler Format:", 
                    value = "Examples: Channaeth Shuuss, Cank Agryg, Xujix Rutt, etc.",
                    inline = False
                )
                character_name_em.description = "Mandalorian Name Generator [Click Here](https://www.dimfuture.net/starwars/random/generate.php)"

                character_name_em.set_thumbnail(
                    url = "https://lumiere-a.akamaihd.net/v1/images/image_3104fc48.jpeg?region=246%2C0%2C1170%2C878&width=960"
                )

                character_name_em.set_footer(
                    text = "You have 5 minutes to respond. Send cancel to cancel"
                )

                await ctx.send(embed = character_name_em)

                try:
                    character_name = str((await client.wait_for('message', check=message_check, timeout=300)).content)
                except:
                    await ctx.send(embed = ran_out_of_time_em)
                    return
                
                if character_name.lower() == "cancel":
                    await ctx.send(embed = cancelled_em)
                    return
                
                for id in userids["userids"]:
                    for chars in users[id]:
                        if character_name.lower() == chars.lower():
                            duplicate_name_em = discord.Embed(
                                title = "Duplicate name detected!",
                                color = discord.Color.red()
                            )
                            duplicate_name_em.add_field(name = f"Your name is identical to {chars}", value = f"That pre-existing character belongs to <@{id}>")
                            duplicate_name_em.set_footer(text = "Command reset")
                            await ctx.send(embed = duplicate_name_em)
                            return
                
                
                faction = "Mandalorian"
                job = job_choice
                legion = "None"
                weapon_choice = []
                armor = "Mandalorian Lightweight Plasteel Armor"
                items = []
                species = "Mandalorian"
                roles = [faction,job]
                money = 2000000
                is_character = "no"
                ships = []

                final_char_layout = discord.Embed(
                    title = f"This is your Character: {character_name}",
                    color = discord.Color.blue()
                )

                final_char_layout.add_field(name = "Faction", value = faction, inline = False)
                final_char_layout.add_field(name = "Job", value = job, inline = True)
                final_char_layout.add_field(name = "Legion", value = legion, inline = False)
                final_char_layout.add_field(name = "Weapon", value = "None", inline = True)
                final_char_layout.add_field(name = "Armor", value = armor, inline = False)
                final_char_layout.add_field(name = "Items", value = "None", inline = False)
                final_char_layout.add_field(name = "Ships", value = "None", inline = False)
                final_char_layout.add_field(name = "Money", value = money, inline = True)
                final_char_layout.add_field(name = "Species", value = species, inline = True)
                final_char_layout.set_footer(icon_url = user.avatar_url, text = "React with '✅' if you are content with your character or '❌' to cancel. You have 60 seconds to respond")

                final_char_message = await ctx.send(embed = final_char_layout)

                await final_char_message.add_reaction("✅")
                await final_char_message.add_reaction("❌")

                try:
                    reaction, reactor = await client.wait_for('reaction_add', check = reaction_check, timeout = 60)
                    go_ahead = str(reaction.emoji)
                except:
                    await ctx.send(embed = ran_out_of_time_em)
                    return
                
                if go_ahead == "❌":
                    await ctx.send(embed = cancelled_em)
                    return
                
                if str(reaction.emoji) not in ["✅","❌"]:
                    await ctx.send(embed = invalid_reaction_em)
                    return
                
                if True:
                    if str(user.id) in users:
                        users[str(user.id)][character_name] = {}
                        users[str(user.id)][character_name]["faction"] = faction
                        users[str(user.id)][character_name]["job"] = job
                        users[str(user.id)][character_name]["legion"] = legion
                        users[str(user.id)][character_name]["weapons"] = weapon_choice
                        users[str(user.id)][character_name]["armor"] = armor
                        users[str(user.id)][character_name]["items"] = items 
                        users[str(user.id)][character_name]["species"] = species
                        users[str(user.id)][character_name]["money"] = money 
                        users[str(user.id)][character_name]["roles"] = roles
                        users[str(user.id)][character_name]["is_character"] = is_character
                        users[str(user.id)][character_name]["ships"] = ships
                        users[str(user.id)][character_name]["units"] = []
                    else:
                        users[str(user.id)] = {}
                        users[str(user.id)][character_name] = {}
                        users[str(user.id)][character_name]["faction"] = faction
                        users[str(user.id)][character_name]["job"] = job
                        users[str(user.id)][character_name]["legion"] = legion
                        users[str(user.id)][character_name]["weapons"] = weapon_choice
                        users[str(user.id)][character_name]["armor"] = armor
                        users[str(user.id)][character_name]["items"] = items 
                        users[str(user.id)][character_name]["species"] = species
                        users[str(user.id)][character_name]["money"] = 0
                        users[str(user.id)][character_name]["roles"] = roles
                        users[str(user.id)][character_name]["is_character"] = is_character
                        users[str(user.id)][character_name]["ships"] = ships
                        users[str(user.id)][character_name]["units"] = []

                with open("users.json", "w") as f:
                    json.dump(users,f,sort_keys=True, indent=4, separators=(',', ': '))
                
                if str(user.id) not in userids["userids"]:
                    userids["userids"].append(str(user.id))
                    with open("userids.json", "w") as f:
                        json.dump(userids,f,sort_keys=True, indent=4, separators=(',', ': '))
                
                data_success = discord.Embed(
                    title = "Data Created Successfully!",
                    color = discord.Color.green()
                )
                await ctx.send(embed = data_success)
                return


#bechar Command
@client.command()
async def bechar(ctx,*,char):
    users = await get_user_data()
    userids = await get_userids()
    user = ctx.author

    list_of_acc = userids["userids"]

    if str(user.id) in list_of_acc:

        for chars in users[str(user.id)]:
            if users[str(user.id)][chars]["is_character"] == "yes":
                for roles in users[str(user.id)][chars]["roles"]:
                    await user.remove_roles(discord.utils.get(user.guild.roles, name=roles))
                users[str(user.id)][chars]["is_character"] = "no"
                with open("users.json", "w") as f:
                    json.dump(users,f,sort_keys=True, indent=4, separators=(',', ': '))
    
        for specchars in users[str(user.id)]:
            if char.lower() == specchars.lower():
                for roles in users[str(user.id)][specchars]["roles"]:
                    await user.add_roles(discord.utils.get(user.guild.roles, name=roles))
                try:
                    await user.edit(nick=specchars)
                except:
                    owner_em = discord.Embed(
                        title = "An error occurred",
                        color = discord.Color.red()
                    )
                    owner_em.add_field(
                        name = "I am missing permission to change your nickname!", 
                        value = "This error could be because you are the owner. Please change your nickname yourself"
                        )
                    await ctx.send(embed = owner_em)
                users[str(user.id)][specchars]["is_character"] = "yes"
                with open("users.json", "w") as f:
                    json.dump(users,f,sort_keys=True, indent=4, separators=(',', ': '))
                success = discord.Embed(
                    title = "Character Transfer Successful!",
                    color = discord.Color.green()
                )
                success.add_field(name = "Character Transfered to:", value = specchars)
                await ctx.send(embed = success)
                return
        
        no_char = discord.Embed(
            title = "Your character was not found!",
            color = discord.Color.red()
        )
        no_char.set_footer(text = "Try checking your spelling")
        await ctx.send(embed = no_char)
    else:
        no_char = discord.Embed(
            title = "You don't have any characters!",
            color = discord.Color.red()
        )
        no_char.set_footer(text = "Please create a character first!")
        await ctx.send(embed = no_char)


#deletechar command
@client.command()
async def deletechar(ctx,*,char = None):
    users = await get_user_data()
    userids = await get_userids()
    user = ctx.author

    if char == None:
        invalid_param = discord.Embed(
            title = "No Parameter was given for character!",
            color = discord.Color.red()
        )

        invalid_param.set_footer(text = "You didn't specify what character you wanted to delete!")
        await ctx.send(embed = invalid_param)
        return 

    def reaction_check(reaction, reactor):
        return reactor == ctx.author 
    
    staff_role = discord.utils.get(user.guild.roles, name="Staff")

    if staff_role in user.roles:

        char_list = []

        for id in userids["userids"]:
            for chars in users[id]:
                char_list.append(chars.lower())
        
        if char.lower() not in char_list: 
            invalid_spelling = discord.Embed(
                title = "That character doesn't exist!",
                color = discord.Color.red()
            )
            invalid_spelling.set_footer(text = "Check your spelling!")
            await ctx.send(embed = invalid_spelling)
            return
        
        confirm_em = discord.Embed(
            title = "Are you sure you want to delete this character? This action cannot be undone",
            color = discord.Color.red()
        )
        confirm_em.add_field(name = "✅ - Yes", value = "** **", inline = False)
        confirm_em.add_field(name = "❌ - No", value = "** **", inline = False)
        confirm_em.set_footer(text = "You have 60 seconds to react")
        
        confirm_msg = await ctx.send(embed = confirm_em)

        await confirm_msg.add_reaction("✅")
        await confirm_msg.add_reaction("❌")

        try:
            reaction, reactor = await client.wait_for('reaction_add', check = reaction_check, timeout = 60)
        except:
            await ctx.send(embed = ran_out_of_time_em)
            return
        
        if str(reaction.emoji) == "❌":                 
            await ctx.send(embed = cancelled_em)
            return

        if str(reaction.emoji) not in ["✅","❌"]:
            await ctx.send(embed = invalid_reaction_em)
            return

        for id in userids["userids"]:
            for chars in users[id]:
                if char.lower() == chars.lower():
                    char = chars
                    id_of_user = id 
        
        try:
            users[id_of_user].pop(char)
            with open("users.json", "w") as f:
                json.dump(users,f,sort_keys=True, indent=4, separators=(',', ': '))
            success = discord.Embed(
                title = "Character Deletion Success!",
                color = discord.Color.green()
            )
            success.set_footer(text = f"The character deleted was {char}")
            await ctx.send(embed = success)
            return 
        except:
            invalid_spelling = discord.Embed(
                title = "That character doesn't exist!",
                color = discord.Color.red()
            )
            invalid_spelling.set_footer(text = "Check your spelling!")
            await ctx.send(embed = invalid_spelling)
            return
        return 
    

    
    charlst = []
    for chars in users[str(user.id)]:
        charlst.append(chars.lower())
    
    if char.lower() not in charlst:
        invalid_spelling = discord.Embed(
            title = "That character doesn't exist!",
            color = discord.Color.red()
        )
        invalid_spelling.set_footer(text = "Check your spelling!")
        await ctx.send(embed = invalid_spelling)
        return

    if str(user.id) in userids["userids"]:
        confirm_em = discord.Embed(
            title = "Are you sure you want to delete your character? This action cannot be undone",
            color = discord.Color.red()
        )
        confirm_em.add_field(name = "✅ - Yes", value = "** **", inline = False)
        confirm_em.add_field(name = "❌ - No", value = "** **", inline = False)
        confirm_em.set_footer(text = "You have 60 seconds to react")
        
        confirm_msg = await ctx.send(embed = confirm_em)

        await confirm_msg.add_reaction("✅")
        await confirm_msg.add_reaction("❌")

        try:
            reaction, reactor = await client.wait_for('reaction_add', check = reaction_check, timeout = 60)
        except:
            await ctx.send(embed = ran_out_of_time_em)
            return
        
        if str(reaction.emoji) == "❌":
            await ctx.send(embed = cancelled_em)
            return

        if str(reaction.emoji) not in ["✅","❌"]:
            await ctx.send(embed = invalid_reaction_em)
            return
        
        for chars in users[str(user.id)]:
            if char.lower() == chars.lower():
                char = chars

        try:
            users[str(user.id)].pop(char)
            with open("users.json", "w") as f:
                json.dump(users,f,sort_keys=True, indent=4, separators=(',', ': '))
            success = discord.Embed(
                title = "Character Deletion Success!",
                color = discord.Color.green()
            )
            success.set_footer(text = f"The character deleted was {char}")
            await ctx.send(embed = success)
            return 
        except:
            invalid_spelling = discord.Embed(
                title = "That character doesn't exist!",
                color = discord.Color.red()
            )
            invalid_spelling.set_footer(text = "Check your spelling!")
            await ctx.send(embed = invalid_spelling)
            return
    else:
        no_char = discord.Embed(
            title = "You don't have any characters!",
            color = discord.Color.red()
        )
        no_char.set_footer(text = "Please create a character first!")
        await ctx.send(embed = no_char)
        return


#charinfo command
@client.command()
async def charinfo(ctx, *, char=None):
    users = await get_user_data()
    userids = await get_userids()
    user = ctx.author 

    if char == None:
        char = user.display_name

    for id in userids["userids"]:
        for chars in users[id]:
            if chars.lower() == char.lower():
                basic_char_em = discord.Embed(
                    title = f"{chars}'s Basic info",
                    color = discord.Color.orange()
                )

                money = users[id][chars]['money']

                s = '%d' % money
                groups = []
                while s and s[-1].isdigit():
                    groups.append(s[-3:])
                    s = s[:-3]
                money = s + ','.join(reversed(groups))

                basic_char_em.add_field(name = "Owner of Character", value = f"<@{id}>", inline = False)
                basic_char_em.add_field(name = "Cash", value = f"<:credits:647021662662819850> {money}", inline = False)
                basic_char_em.add_field(name = "Species", value = users[id][chars]['species'], inline = False)
                basic_char_em.add_field(name = "Armor", value = users[id][chars]['armor'], inline = False)

                faction_char_em = discord.Embed(
                    title = f"{chars}'s Faction Info",
                    color = discord.Color.dark_blue()
                )

                faction_char_em.add_field(name = "Faction", value = users[id][chars]['faction'], inline = False)
                faction_char_em.add_field(name = "Job", value = users[id][chars]['job'], inline = False)
                faction_char_em.add_field(name = "Legion", value = users[id][chars]['legion'], inline = False)

                inv_char_em = discord.Embed(
                    title = f"{chars}'s Inventory",
                    color = discord.Color.dark_gold()
                )
                
                item_lst = users[id][chars]['items']
                weapon_lst = users[id][chars]['weapons']
                ship_lst = users[id][chars]['ships']
                unit_lst = users[id][chars]['units']

                item_dict = Counter(item_lst)
                item_string = ""

                for key,value in item_dict.items():
                    item_string += f"\n{value} - {key}"
                
                if bool(item_lst) == False:
                    item_string = "None"

                inv_char_em.add_field(name = "Items:", value = item_string, inline = False)



                weapon_dict = Counter(weapon_lst)
                weapon_string = ""

                for key,value in weapon_dict.items():
                    weapon_string += f"\n{value} - {key}"

                if bool(weapon_lst) == False:
                    weapon_string = "None"                

                inv_char_em.add_field(name = "Weapons:", value = weapon_string, inline = False)



                ship_dict = Counter(ship_lst)
                ship_string = ""

                for key,value in ship_dict.items():
                    ship_string += f"\n{value} - {key}"

                if bool(ship_lst) == False:
                    ship_string = "None"

                inv_char_em.add_field(name = "Ships:", value = ship_string, inline = False)



                unit_dict = Counter(unit_lst)
                unit_string = ""

                for key,value in unit_dict.items():
                    unit_string += f"\n{value} - {key}"

                if bool(unit_lst) == False:
                    unit_string = "None"

                inv_char_em.add_field(name = "Units:", value = unit_string, inline = False)
                await ctx.send(embed = basic_char_em)
                await ctx.send(embed = faction_char_em)
                await ctx.send(embed = inv_char_em)
                return
                
    no_char = discord.Embed(
        title = "That character was not found!",
        color = discord.Color.red()
    )
    no_char.add_field(name = "Command Syntax:", value = ">charinfo <character name>")
    no_char.set_footer(text = "Try checking the spelling of the character name you want to check")
    await ctx.send(embed = no_char)


#Balance command
@client.command(aliases = ["bal"])
async def balance(ctx,*,char=None):
    users = await get_user_data()
    userids = await get_userids()
    user = ctx.author

    if char == None:
        char = user.display_name
    
    if str(user.id) not in userids["userids"]:
        no_char = discord.Embed(
            title = "You don't have any characters!",
            color = discord.Color.red()
        )

        no_char.set_footer(text = "Try creating a character with the createchar command first!")
        await ctx.send(embed = no_char)
        return

    for id in userids["userids"]:
        for chars in users[id]:
            if chars.lower() == char.lower():
                bal_em = discord.Embed(
                    title = f"{char}'s Balance",
                    color = discord.Color.blue()
                )
                money = users[id][chars]["money"]

                s = '%d' % money
                groups = []
                while s and s[-1].isdigit():
                    groups.append(s[-3:])
                    s = s[:-3]
                money = s + ','.join(reversed(groups))


                bal_em.add_field(name = "Balance:", value = f"<:credits:647021662662819850>{money}")
                await ctx.send(embed = bal_em)
                return

    no_char = discord.Embed(
        title = "That character was not found!",
        color = discord.Color.red()
    )
    no_char.add_field(name = "Command Syntax:", value = ">balance/bal <character name>")
    no_char.set_footer(text = "Try checking the spelling of the character name you want to check")
    await ctx.send(embed = no_char)


#Inventory command
@client.command(aliases = ["inv"])
async def inventory(ctx,*,char=None):
    users = await get_user_data()
    userids = await get_userids()
    user = ctx.author

    if char == None:
        char = user.display_name
    
    if str(user.id) not in userids["userids"]:
        no_char = discord.Embed(
            title = "You don't have any characters!",
            color = discord.Color.red()
        )

        no_char.set_footer(text = "Try creating a character with the createchar command first!")
        await ctx.send(embed = no_char)
        return

    for id in userids["userids"]:
        for chars in users[id]:
            if chars.lower() == char.lower():
                inv_char_em = discord.Embed(
                    title = f"{chars}'s Inventory",
                    color = discord.Color.blue()
                )
                
                item_lst = users[id][chars]['items']
                weapon_lst = users[id][chars]['weapons']
                ship_lst = users[id][chars]['ships']
                unit_lst = users[id][chars]['units']

                item_dict = Counter(item_lst)
                item_string = ""

                for key,value in item_dict.items():
                    item_string += f"\n{value} - {key}"
                
                if bool(item_lst) == False:
                    item_string = "None"

                inv_char_em.add_field(name = "Items:", value = item_string, inline = False)



                weapon_dict = Counter(weapon_lst)
                weapon_string = ""

                for key,value in weapon_dict.items():
                    weapon_string += f"\n{value} - {key}"

                if bool(weapon_lst) == False:
                    weapon_string = "None"                

                inv_char_em.add_field(name = "Weapons:", value = weapon_string, inline = False)



                ship_dict = Counter(ship_lst)
                ship_string = ""

                for key,value in ship_dict.items():
                    ship_string += f"\n{value} - {key}"

                if bool(ship_lst) == False:
                    ship_string = "None"

                inv_char_em.add_field(name = "Ships:", value = ship_string, inline = False)



                unit_dict = Counter(unit_lst)
                unit_string = ""

                for key,value in unit_dict.items():
                    unit_string += f"\n{value} - {key}"

                if bool(unit_lst) == False:
                    unit_string = "None"

                inv_char_em.add_field(name = "Units:", value = unit_string, inline = False)
                await ctx.send(embed = inv_char_em)
                return

    no_char = discord.Embed(
        title = "That character was not found!",
        color = discord.Color.red()
    )
    no_char.add_field(name = "Command Syntax:", value = ">inventory/inv <character name>")
    no_char.set_footer(text = "Try checking the spelling of the character name you want to check")
    await ctx.send(embed = no_char)
    
    
@client.command(aliases = ["displaychar"])
async def displaychars(ctx, member : discord.Member = None):

    users = await get_user_data()
    userids = await get_userids()
    
    if member == None:
        user = ctx.author
    else:
        user = member
    
    if str(user.id) not in userids["userids"]:
        no_chars = discord.Embed(

            title = f"{user} has no characters to display!",
            color = discord.Color.red()

            )
        no_chars.set_footer(text = "Create a character with the >createchar command!")
        await ctx.send(embed = no_chars)
        return

    elif bool(users[str(user.id)]) == False:
        no_chars = discord.Embed(

            title = "You have no characters to display!",
            color = discord.Color.red()

            )
        no_chars.set_footer(text = "Create a character with the >createchar command!")
        await ctx.send(embed = no_chars)
        return
    
    char_list = ""

    for char in users[str(user.id)]:
        char_list += f"\n - {char}"
    
    char_list_em = discord.Embed(
        title = f"List of {user}'s Characters",
        color = discord.Color.blue()
    )

    char_list_em.add_field(name = "** **", value = char_list, inline = False)

    char_list_em.set_footer(text = "Check specific a character's information with the >charinfo command!")

    await ctx.send(embed = char_list_em)

#Error Handling for >displaychars command
@displaychars.error
async def displaychars_error(ctx,error):
    if isinstance(error, commands.MemberNotFound):
        mem_error = discord.Embed(
            title = "I couldn't find that member!",
            color = discord.Color.red()
        )
        mem_error.set_footer(text = "Syntax: >displaychars <@member>")
        await ctx.send(mem_error)
        return


#Sell Item
@client.command()
async def sell(ctx, member : discord.Member = None, *, item = None):
    if member == None:
        no_member = discord.Embed(
            title = "You didn't specify any member!",
            color = discord.Color.red()
        )
        no_member.set_footer(text = "Syntax: >sell <@member> <item name>")
        await ctx.send(embed = no_member)
        return

    elif item == None:
        no_item = discord.Embed(
            title = "You didn't specify any item you want to sell!",
            color = discord.Color.red()
        )
        no_item.set_footer(text = "Syntax: >sell <@member> <item name>")
        await ctx.send(embed = no_item)
        return


@sell.error
async def sell_error(ctx,error):
    if isinstance(error, commands.MemberNotFound):
        mem_error = discord.Embed(
            title = "I couldn't find that member!",
            color = discord.Color.red()
        )
        mem_error.set_footer(text = "Syntax: >sell <@member> <item name>")
        await ctx.send(mem_error)
        return


"""
ECONOMY COMMANDS
"""
@client.command(aliases = ["purchase"])
async def buy(ctx,*, purchasable = None):

    if purchasable == None:
        invalid_em = discord.Embed(
            title = "You didn't specify what you wanted to purchase!",
            color = discord.Color.red()
        )
        invalid_em.set_footer(text = "Syntax: >buy <item name>")
        await ctx.send(embed = invalid_em)
        return


    not_enough_money = discord.Embed(
        title = "You don't have enough money to purchase this!",
        color = discord.Color.red()
    )
    
    user = ctx.author
    users = await get_user_data()
    userids = await get_userids()
    store = await get_store()
    character = "None"

    sections = ["item","ship","unit","weapon"]

    if str(user.id) in userids["userids"]:

        if bool(users[str(user.id)]) != False:

            for char in users[str(user.id)]:

                if users[str(user.id)][char]["is_character"] == "yes":
                    
                    for section in sections:

                        for item in store[section]:

                            if purchasable.lower() == item.lower():

                                rolelist = []

                                for role in user.roles:
                                    if role != ctx.guild.default_role:
                                        rolelist.append(role.mention)
                                

                                stock = store[section][item]["stock"] 
                                price = store[section][item]["price"] 
                                usr_money = users[str(user.id)][char]["money"]

                                if stock == "infinity":
                                    if section == "unit":
                                        gm = discord.utils.get(user.guild.roles, name="Guild/Syndicate/Crime/Militia Leader")
                                        roles_needed = store[section][item]["roles"]

                                        if gm in user.roles:

                                            if roles_needed == "None":
                                                usr_money -= price

                                                if usr_money < 0:
                                                    await ctx.send(embed=not_enough_money)
                                                    return
                                                else:
                                                    users[str(user.id)][char]["units"].append(item)
                                                    users[str(user.id)][char]["money"] = usr_money

                                                with open("users.json", "w") as f:
                                                    json.dump(users, f, sort_keys=True,
                                                            indent=4, separators=(',', ': '))

                                                purchase_success = discord.Embed(
                                                     title="Purchase successful!",
                                                    color=discord.Color.green()
                                                )
                                                await ctx.send(embed=purchase_success)
                                                return
                                                
                                            else:
                                                for role in rolelist:
                                                    if role in roles_needed:

                                                        usr_money -= price

                                                        if usr_money < 0:
                                                            await ctx.send(embed = not_enough_money)
                                                            return
                                                        else:
                                                            users[str(user.id)][char]["units"].append(item)
                                                            users[str(user.id)][char]["money"] = usr_money

                                                        with open("users.json", "w") as f:
                                                            json.dump(users,f,sort_keys=True, indent=4, separators=(',', ': '))
                                                        
                                                        purchase_success = discord.Embed(
                                                            title = "Purchase successful!",
                                                            color = discord.Color.green()
                                                        )
                                                        await ctx.send(embed = purchase_success)
                                                        return
                                                        

                                                missing_role = discord.Embed(
                                                    title = "You are missing at least one of the required roles!",
                                                    color = discord.Color.red()
                                                )
                                                roles_neededstr = ""
                                                for role in roles_needed:
                                                    roles_neededstr += f"\n-{role}"

                                                missing_role.add_field(name = "Missing roles:", value = roles_neededstr)
                                                await ctx.send(embed = missing_role)
                                                return

                                        else:
                                            missing_role = discord.Embed(
                                                title = "You are missing a role!",
                                                color = discord.Color.red()
                                            )
                                            missing_role.add_field(name = "Required Role:", value = f"- {gm.mention}")
                                            missing_role.set_footer(text = "You are required to have at least the Guild/Syndicate/Crime/Militia Leader role before purchasing anything from the unit store")
                                            await ctx.send(embed = missing_role)
                                            return


                                                
                                    else:
                                        section_dict = {
                                            "weapon" : "weapons",
                                            "ship" : "ships",
                                            "item" : "items"
                                        }

                                        roles_needed = store[section][item]["roles"]

                                        if roles_needed == "None":
                                            usr_money -= price

                                            if usr_money < 0:
                                                await ctx.send(embed=not_enough_money)
                                                return
                                            else:
                                                users[str(user.id)][char][section_dict[section]].append(item)
                                                users[str(user.id)][char]["money"] = usr_money

                                            with open("users.json", "w") as f:
                                                json.dump(users, f, sort_keys=True,
                                                        indent=4, separators=(',', ': '))

                                            purchase_success = discord.Embed(
                                                    title="Purchase successful!",
                                                color=discord.Color.green()
                                            )
                                            await ctx.send(embed=purchase_success)
                                            return
                                            
                                        else:
                                            for role in rolelist:
                                                if role in roles_needed:

                                                    usr_money -= price

                                                    if usr_money < 0:
                                                        await ctx.send(embed = not_enough_money)
                                                        return
                                                    else:
                                                        users[str(user.id)][char][section_dict[section]].append(item)
                                                        users[str(user.id)][char]["money"] = usr_money

                                                    with open("users.json", "w") as f:
                                                        json.dump(users,f,sort_keys=True, indent=4, separators=(',', ': '))
                                                    
                                                    purchase_success = discord.Embed(
                                                        title = "Purchase successful!",
                                                        color = discord.Color.green()
                                                    )
                                                    await ctx.send(embed = purchase_success)
                                                    return
                                                    

                                            missing_role = discord.Embed(
                                                title = "You are missing at least one of the required roles!",
                                                color = discord.Color.red()
                                            )
                                            roles_neededstr = ""
                                            for role in roles_needed:
                                                roles_neededstr += f"\n-{role}"

                                            missing_role.add_field(name = "Missing roles:", value = roles_neededstr)
                                            await ctx.send(embed = missing_role)
                                            return

                                elif stock -1 >= 0:
                                    if section == "unit":
                                        gm = discord.utils.get(user.guild.roles, name="Guild/Syndicate/Crime/Militia Leader")
                                        roles_needed = store[section][item]["roles"]

                                        if gm in user.roles:

                                            if roles_needed == "None":
                                                usr_money -= price

                                                if usr_money < 0:
                                                    await ctx.send(embed=not_enough_money)
                                                    return
                                                else:
                                                    users[str(user.id)][char]["units"].append(item)
                                                    users[str(user.id)][char]["money"] = usr_money
                                                    store[section][item]["stock"] -= 1

                                                with open("users.json", "w") as f:
                                                    json.dump(users, f, sort_keys=True,
                                                            indent=4, separators=(',', ': '))
                                                
                                                with open("store.json", "w") as f:
                                                    json.dump(store, f, sort_keys=True,
                                                            indent=4, separators=(',', ': '))

                                                purchase_success = discord.Embed(
                                                     title="Purchase successful!",
                                                    color=discord.Color.green()
                                                )
                                                await ctx.send(embed=purchase_success)
                                                return
                                                
                                            else:
                                                for role in rolelist:
                                                    if role in roles_needed:

                                                        usr_money -= price

                                                        if usr_money < 0:
                                                            await ctx.send(embed = not_enough_money)
                                                            return
                                                        else:
                                                            users[str(user.id)][char]["units"].append(item)
                                                            users[str(user.id)][char]["money"] = usr_money

                                                        with open("users.json", "w") as f:
                                                            json.dump(users,f,sort_keys=True, indent=4, separators=(',', ': '))
                                                        
                                                        purchase_success = discord.Embed(
                                                            title = "Purchase successful!",
                                                            color = discord.Color.green()
                                                        )
                                                        await ctx.send(embed = purchase_success)
                                                        return
                                                        

                                                missing_role = discord.Embed(
                                                    title = "You are missing at least one of the required roles!",
                                                    color = discord.Color.red()
                                                )
                                                roles_neededstr = ""
                                                for role in roles_needed:
                                                    roles_neededstr += f"\n-{role}"

                                                missing_role.add_field(name = "Missing roles:", value = roles_neededstr)
                                                await ctx.send(embed = missing_role)
                                                return

                                        else:
                                            missing_role = discord.Embed(
                                                title = "You are missing a role!",
                                                color = discord.Color.red()
                                            )
                                            missing_role.add_field(name = "Required Role:", value = f"- {gm.mention}")
                                            missing_role.set_footer(text = "You are required to have at least the Guild/Syndicate/Crime/Militia Leader role before purchasing anything from the unit store")
                                            await ctx.send(embed = missing_role)
                                            return


                                                
                                    else:
                                        section_dict = {
                                            "weapon" : "weapons",
                                            "ship" : "ships",
                                            "item" : "items"
                                        }

                                        roles_needed = store[section][item]["roles"]

                                        if roles_needed == "None":
                                            usr_money -= price

                                            if usr_money < 0:
                                                await ctx.send(embed=not_enough_money)
                                                return
                                            else:
                                                users[str(user.id)][char][section_dict[section]].append(item)
                                                users[str(user.id)][char]["money"] = usr_money
                                                store[section][item]["stock"] -= 1

                                            with open("users.json", "w") as f:
                                                json.dump(users, f, sort_keys=True,
                                                        indent=4, separators=(',', ': '))
                                            
                                            with open("store.json", "w") as f:
                                                    json.dump(store, f, sort_keys=True,
                                                            indent=4, separators=(',', ': '))

                                            purchase_success = discord.Embed(
                                                    title="Purchase successful!",
                                                color=discord.Color.green()
                                            )
                                            await ctx.send(embed=purchase_success)
                                            return
                                            
                                        else:
                                            for role in rolelist:
                                                if role in roles_needed:

                                                    usr_money -= price

                                                    if usr_money < 0:
                                                        await ctx.send(embed = not_enough_money)
                                                        return
                                                    else:
                                                        users[str(user.id)][char][section_dict[section]].append(item)
                                                        users[str(user.id)][char]["money"] = usr_money
                                                        store[section][item]["stock"] -= 1

                                                    with open("users.json", "w") as f:
                                                        json.dump(users,f,sort_keys=True, indent=4, separators=(',', ': '))

                                                    with open("store.json", "w") as f:
                                                        json.dump(store, f, sort_keys=True,
                                                            indent=4, separators=(',', ': '))
                                                    
                                                    
                                                    
                                                    
                                                    purchase_success = discord.Embed(
                                                        title = "Purchase successful!",
                                                        color = discord.Color.green()
                                                    )
                                                    await ctx.send(embed = purchase_success)
                                                    return
                                                    

                                            missing_role = discord.Embed(
                                                title = "You are missing at least one of the required roles!",
                                                color = discord.Color.red()
                                            )
                                            roles_neededstr = ""
                                            for role in roles_needed:
                                                roles_neededstr += f"\n-{role}"

                                            missing_role.add_field(name = "Missing roles:", value = roles_neededstr)
                                            await ctx.send(embed = missing_role)
                                            return
                                    
                                else:
                                    out_of_stock = discord.Embed(
                                        title = "That item is out of stock!",
                                        color = discord.Color.red()
                                    )
                                    out_of_stock.set_footer(text = "Please ask a Staff member to restock this item if required!")
                                    await ctx.send(embed = out_of_stock)
                                    return


                    item_not_found = discord.Embed(
                        title = "That item was not found!",
                        color = discord.Color.red()
                    )
                    item_not_found.set_footer(text = "Try checking your spelling or looking at the shop!")
                    await ctx.send(embed = item_not_found)
                    return
                                
            
            not_rping_as_char = discord.Embed(
                title = "You are currently not using any character!",
                color = discord.Color.red()
            )
            not_rping_as_char.set_footer(text = "This means you can't purchase anything! RP as a character with the >bechar <you character name> command!")
            await ctx.send(embed = not_rping_as_char)
            return  

        else: 
            no_char = discord.Embed(
            title = "You don't have any characters!",
            color = discord.Color.red()
        )
        no_char.set_footer(text = "Please create a character first!")
        await ctx.send(embed = no_char)
        return

    else:
        no_char = discord.Embed(
            title = "You don't have any characters!",
            color = discord.Color.red()
        )
        no_char.set_footer(text = "Please create a character first!")
        await ctx.send(embed = no_char)
        return
        


    if str(user.id) in userids["userids"]:
        for char in users[str(user.id)]:
            if users[str(user.id)][char]["is_character"] == "yes":
                pass

        no_char = discord.Embed(
            title = "You aren't roleplaying as any character yet!",
            color = discord.Color.red()
        )
        no_char.set_footer(text = "Please use the !bechar command to become a character first!")
        await ctx.send(embed = no_char)
        return

    else:
        no_char = discord.Embed(
            title = "You don't have any characters!",
            color = discord.Color.red()
        )
        no_char.set_footer(text = "Please create a character first!")
        await ctx.send(embed = no_char)
        return


@client.command(aliases = ["shop"])
async def store(ctx, section = None):
    
    if section == None:
        invalid_em = discord.Embed(
            title = "You haven't identified which part of the store you would like to see!",
            color = discord.Color.red()
        )
        invalid_em.add_field(name = "Available Sections:", value = f"- Items\n- Weapons\n- Ships\n - Units (Only available for <@&711846263758389299>)")
        invalid_em.set_footer(text = "Syntax: >store <section>")
        await ctx.send(embed = invalid_em)
        return

    elif section.lower() not in ["item","items","weapon","weapons","ship","ships","unit","units"]:
        section_not_found = discord.Embed(
            title = "I couldn't find that section!",
            color = discord.Color.red()
        )
        section_not_found.set_footer(text = "The only sections in the shop are items, weapons, ships, and units!")
        await ctx.send(embed = section_not_found)
        return



    store = await get_store()
    store_board = {}

    if section.lower() == "item" or section.lower() == "items":
        for item in store["item"]:
            name = item
            amount = store["item"][item]["price"]
            store_board[name] = amount 

        store_list = sorted(store_board, key=store_board.get, reverse=False)

        shop_em = discord.Embed(
            title = "Item Store",
            color = discord.Color.dark_blue()
        )
        for item in store_list:
            price = store_board[item]

            s = '%d' % price
            groups = []
            while s and s[-1].isdigit():
                groups.append(s[-3:])
                s = s[:-3]
            price = s + ','.join(reversed(groups))
           
            
            shop_em.add_field(
                name = f"<:credits:647021662662819850>{price} - {item}",
                value = "** **",
                inline = False
            )
        await ctx.send(embed = shop_em)

    elif section.lower() == "weapon" or section.lower() == "weapons":
        for item in store["weapon"]:
            name = item
            amount = store["weapon"][item]["price"]
            store_board[name] = amount 

        store_list = sorted(store_board, key=store_board.get, reverse=False)

        shop_em = discord.Embed(
            title = "Weapon Store",
            color = discord.Color.dark_blue()
        )
        for item in store_list:
            price = store_board[item]

            s = '%d' % price
            groups = []
            while s and s[-1].isdigit():
                groups.append(s[-3:])
                s = s[:-3]
            price = s + ','.join(reversed(groups))

            shop_em.add_field(
                name = f"<:credits:647021662662819850>{price} - {item}",
                value = "** **",
                inline = False
            )
        await ctx.send(embed = shop_em)

    elif section.lower() == "ship" or section.lower() == "ships":
        for item in store["ship"]:
            name = item
            amount = store["ship"][item]["price"]
            store_board[name] = amount 

        store_list = sorted(store_board, key=store_board.get, reverse=False)

        shop_em = discord.Embed(
            title = "Ship Store",
            color = discord.Color.dark_blue()
        )
        for item in store_list:
            price = store_board[item]

            s = '%d' % price
            groups = []
            while s and s[-1].isdigit():
                groups.append(s[-3:])
                s = s[:-3]
            price = s + ','.join(reversed(groups))

            shop_em.add_field(
                name = f"<:credits:647021662662819850>{price} - {item}",
                value = "** **",
                inline = False
            )
        await ctx.send(embed = shop_em)

    elif section.lower() == "unit" or section.lower() == "units":
        for item in store["unit"]:
            name = item
            amount = store["unit"][item]["price"]
            store_board[name] = amount 

        store_list = sorted(store_board, key=store_board.get, reverse=False)

        shop_em = discord.Embed(
            title = "Unit Store",
            color = discord.Color.dark_blue()
        )
        for item in store_list:
            price = store_board[item]

            s = '%d' % price
            groups = []
            while s and s[-1].isdigit():
                groups.append(s[-3:])
                s = s[:-3]
            price = s + ','.join(reversed(groups))

            shop_em.add_field(
                name = f"<:credits:647021662662819850>{price} - {item}",
                value = "** **",
                inline = False
            )
        await ctx.send(embed = shop_em)




#Adding stuff to the shop
@client.command()
async def createitem(ctx):
    user = ctx.author
    role_needed = discord.utils.get(user.guild.roles, name="Staff")

    if role_needed not in user.roles:
        invalid_em = discord.Embed(
            title = "You don't have the role required to use this command!",
            color = discord.Color.red()
            )
        invalid_em.add_field(name = "Role Required:", value = "<@&655450923111415819> | If you have a suggestion for an item, post it in <#643742393744621624>")

        await ctx.send(embed = invalid_em)
        return


    store = await get_store()

    def message_check(message):
        return message.author == ctx.author and message.channel == ctx.channel

    def reaction_check(reaction, reactor):
        return reactor == ctx.author 
    

    name_em = discord.Embed(
        title = "What is the name of the item?",
        color = discord.Color.blue()
    )

    name_em.set_footer(text = "Reply cancel to cancel. You have 300 seconds")

    await ctx.send(embed = name_em)

    try:
        item_name = str((await client.wait_for('message', check=message_check, timeout=300)).content)
    except:
        await ctx.send(embed = ran_out_of_time_em)
        return
    
    if item_name.lower() == "cancel":
        await ctx.send(embed = cancelled_em)
        return
    
    for item in store["item"]:
        if item.lower() == item_name.lower():
            duplicate_em = discord.Embed(
                title = "There is already an item by that name!",
                color = discord.Color.red()
            )
            duplicate_em.add_field(
                name = f"The duplicate item is named {item}, and is located in the **ITEM** section of the store",
                value = "** **"
            )
            await ctx.send(embed = duplicate_em)
            return

    for item in store["weapon"]:
        if item.lower() == item_name.lower():
            duplicate_em = discord.Embed(
                title = "There is already an item by that name!",
                color = discord.Color.red()
            )
            duplicate_em.add_field(
                name = f"The duplicate item is named {item}, and is located in the **WEAPON** section of the store",
                value = "** **"
            )
            await ctx.send(embed = duplicate_em)
            return
    
    for item in store["ship"]:
        if item.lower() == item_name.lower():
            duplicate_em = discord.Embed(
                title = "There is already an item by that name!",
                color = discord.Color.red()
            )
            duplicate_em.add_field(
                name = f"The duplicate item is named {item}, and is located in the **SHIP** section of the store",
                value = "** **"
            )
            await ctx.send(embed = duplicate_em)
            return
    
    for item in store["unit"]:
        if item.lower() == item_name.lower():
            duplicate_em = discord.Embed(
                title = "There is already an item by that name!",
                color = discord.Color.red()
            )
            duplicate_em.add_field(
                name = f"The duplicate item is named {item}, and is located in the **UNIT** section of the store",
                value = "** **"
            )
            await ctx.send(embed = duplicate_em)
            return
    
    item_description_em = discord.Embed(
        title = "What is the description of the item?",
        color = discord.Color.blue()
    )
    item_description_em.set_footer(text = "Reply cancel to cancel. You have 300 seconds")
    await ctx.send(embed = item_description_em)

    try:
        item_description = str((await client.wait_for('message', check=message_check, timeout=300)).content)
    except:
        await ctx.send(embed = ran_out_of_time_em)
        return
    
    if item_description.lower() == "cancel":
        await ctx.send(embed = cancelled_em)
        return

    item_class_em = discord.Embed(
        title = "What is the class of this item?",
        color = discord.Color.blue()
    )

    item_class_em.add_field(
        name = "🟦 - Item (Grenades, Accessories, e.g: Thermal Detonator, Ship Repair Kit, Jetpack)",
        value = "** **",
        inline = False
    )

    item_class_em.add_field(
        name = "🟥 - Weapon (Blasters, Slugthrowers, Melee, e.g: Vibroblade, Scattergun, EE-3 Carbine Rifle)",
        value = "** **",
        inline = False
    )

    item_class_em.add_field(
        name = "🟧 - Ship (Starfigher, Cruiser, Space Station, e.g: YT-1300 light freighter, G-1A Starfighter, Kom'rk-class fighter)",
        value = "** **",
        inline = False
    )

    item_class_em.add_field(
        name = "🟨 - Unit (Soldiers, Pilots, e.g: Foot Trooper Unit, Jetpack Unit",
        value = "** **",
        inline = False
    )

    item_class_em.add_field(
        name = "❌ - Cancel",
        value = "** **",
        inline = False
    )

    item_class_em.set_footer(text = "You have 300 seconds")


    item_class_msg = await ctx.send(embed = item_class_em)

    await item_class_msg.add_reaction("🟦")
    await item_class_msg.add_reaction("🟥")
    await item_class_msg.add_reaction("🟧")
    await item_class_msg.add_reaction("🟨")
    await item_class_msg.add_reaction("❌")

    try:
        reaction, reactor = await client.wait_for('reaction_add', check = reaction_check, timeout = 300)
        item_class_reaction = str(reaction.emoji)
    except:
        await ctx.send(embed = ran_out_of_time_em)
        return
    
    if item_class_reaction == "❌":
        await ctx.send(embed = cancelled_em)
        return
    elif item_class_reaction not in ["🟦","🟥","🟧","🟨","❌"]:
        await ctx.send(embed = invalid_em)
        return
    
    itemDict = {
        "🟦" : "item",
        "🟥" : "weapon",
        "🟧" : "ship",
        "🟨" : "unit"
    }

    item_class = itemDict[item_class_reaction]

    price_em = discord.Embed(
        title = "What is the price of the item?",
        color = discord.Color.blue()
    )

    price_em.set_footer(text = "Send cancel to cancel. You have 300 seconds")

    await ctx.send(embed = price_em)
    
    try:
        item_price = str((await client.wait_for('message', check=message_check, timeout=300)).content)
    except:
        await ctx.send(embed = ran_out_of_time_em)
        return

    if item_price.lower() == "cancel":
        await ctx.send(embed = cancelled_em)
        return
    
    item_price = item_price.replace(",","")

    try:
        item_price = int(item_price)
    except:
        invalid_num_em = discord.Embed(
            title = "That price is not a number!",
            color = discord.Color.red()
        )
        invalid_num_em.set_footer(text = "Command Reset!")
        await ctx.send(embed = invalid_num_em)
        return
    
    roles_required = discord.Embed(
        title = "What roles does the user need to purchase this item?",
        color = discord.Color.blue()
    )

    roles_required.add_field(name = "Mention the roles the user would need to purchase this item", value = "** **")

    roles_required.add_field(name = "Send 'None' if no role is required to purchase this item", value = "** **", inline = False)

    roles_required.set_footer(text = "DISCLAIMER: The user will only need at least 1 of the specified roles to be able to purchase this item. Send cancel to cancel. You have 300 seconds.")

    await ctx.send(embed = roles_required)

    try:
        roles_required = str((await client.wait_for('message', check=message_check, timeout=300)).content)
    except:
        await ctx.send(embed = ran_out_of_time_em)
        return
    
    if roles_required.lower() == "cancel":
        await ctx.send(embed = cancelled_em)
        return
    elif roles_required.lower() == "none":
        roles_required = "None"
        roles_required_2 = "None"
    else:
        roles_required = roles_required.split()

        for role in roles_required:
            if role[:3] != "<@&":
                invalid_em_roles = discord.Embed(
                    title = "Invalid Roles Mentioned!",
                    color = discord.Color.red()
                )

                invalid_em_roles.add_field(name = "You did not mention an actual role! Please try again!", value = "** **")
                await ctx.send(embed = invalid_em_roles)
                return

        roles_required_2 = ""


        for role in roles_required:
            roles_required_2 += f"\n- {role}"
    
    stock_em = discord.Embed(
        title = "What should the stock of this item be?",
        color = discord.Color.blue()
    )

    stock_em.description = "This determines how much of this item is available in the stock. If this item runs out of stock, it will no longer appear in the shop"
    stock_em.set_footer(text = "Reply with any number. Reply with 'None','Infinity' or 'Unlimited' if this item has infinite stock. You have 300 seconds. Reply cancel to cancel")
    
    await ctx.send(embed = stock_em)

    try:
        stock = str((await client.wait_for('message', check=message_check, timeout=300)).content)
    except:
        await ctx.send(embed = ran_out_of_time_em)
        return

    if stock.lower() == "cancel":
        await ctx.send(embed = cancelled_em)
        return
    elif stock.lower() == "none" or stock.lower() == "infinity" or stock.lower() == "unlimited":
        stock = "infinity"
    else:
        try:
            stock = int(stock)
        except:
            invalid_stock_em = discord.Embed(
                title = "That isn't a number!",
                color = discord.Color.red()
            )
            invalid_stock_em.set_footer(text = "Command Reset!")
            await ctx.send(embed = invalid_stock_em)
            return

    name = item_name
    description = item_description
    type_class = item_class 
    item_price = item_price
    stock = stock 

    if type(stock) == int:
        s = '%d' % stock
        groups = []
        while s and s[-1].isdigit():
            groups.append(s[-3:])
            s = s[:-3]
        stock2 = s + ','.join(reversed(groups))

    

    s = '%d' % item_price
    groups = []
    while s and s[-1].isdigit():
        groups.append(s[-3:])
        s = s[:-3]
    price = s + ','.join(reversed(groups))
    
    final_item_em = discord.Embed(
        title = f"{name} Info",
        color = discord.Color.blue()
    )

    final_item_em.add_field(name = "Description:", value = description, inline = False)
    final_item_em.add_field(name = "Class:", value = type_class, inline = False)
    final_item_em.add_field(name = "Price:", value = f"<:credits:647021662662819850> {price}",inline = False)
    final_item_em.add_field(name = "Stock:", value = stock2, inline = False)
    final_item_em.add_field(name = "Roles Required", value = roles_required_2, inline = False)

    final_item_em.set_footer(text = "Confirm by reacting with either ✅ or ❌. You have 300 seconds")
    final_msg = await ctx.send(embed = final_item_em)

    await final_msg.add_reaction("✅")
    await final_msg.add_reaction("❌")

    try:
        reaction, reactor = await client.wait_for('reaction_add', check = reaction_check, timeout = 300)
        confirm_reaction = str(reaction.emoji)
    except:
        await ctx.send(embed = ran_out_of_time_em)
        return
    
    if confirm_reaction not in ["✅","❌"]:
        await ctx.send(embed = invalid_reaction_em)
        return 
    elif confirm_reaction == "❌":
        await ctx.send(embed = cancelled_em)
        return 
    
    store[item_class][name] = {}
    store[item_class][name]["price"] = int(item_price)
    store[item_class][name]["description"] = description
    store[item_class][name]["class"] = type_class
    store[item_class][name]["roles"] = roles_required
    store[item_class][name]["stock"] = stock

    with open("store.json", "w") as f:
        json.dump(store,f,sort_keys=True, indent=4, separators=(',', ': '))
    
    success_em = discord.Embed(
        title = "Successfully Added!",
        color = discord.Color.green()
    )

    await ctx.send(embed = success_em)
    


#Item info command
@client.command()
async def iteminfo(ctx,*,item=None):
    store = await get_store()
    if item == None:
        no_param_specified = discord.Embed(
            title = "You didn't identify an item you want information on!",
            color = discord.Color.red()
        )
        no_param_specified.set_footer(text = "Syntax: >iteminfo <item name>")
        await ctx.send(embed = no_param_specified)
        return
     
    store_sections = ["item","ship","unit","weapon"]
    
    for section in store_sections:
        for things in store[section]:
            if things.lower() == item.lower():

                class_info = store[section][things]["class"].capitalize()
                price = store[section][things]["price"]
                roles_required = store[section][things]["roles"]
                roles_required2 = ""
                stock = store[section][things]["stock"]

                if isinstance(roles_required,list):
                    for role in roles_required:
                        roles_required2 += f"\n- {role}"
                else:
                    roles_required2 = roles_required
                
                if isinstance(stock,int):
                    s = '%d' % stock
                    groups = []
                    while s and s[-1].isdigit():
                        groups.append(s[-3:])
                        s = s[:-3]
                    stock = s + ','.join(reversed(groups))
                else:
                    stock = stock.capitalize()


                s = '%d' % price
                groups = []
                while s and s[-1].isdigit():
                    groups.append(s[-3:])
                    s = s[:-3]
                price2 = s + ','.join(reversed(groups))



            
                iteminfo_em = discord.Embed(
                    title = f"{things}",
                    color = discord.Color.green()
                )
                iteminfo_em.add_field(name = "Description:", value = store[section][things]["description"], inline = False)
                iteminfo_em.add_field(name = "Price:", value = f"<:credits:647021662662819850> {price2}", inline = False)
                iteminfo_em.add_field(name = "Class:", value = class_info, inline = False)
                iteminfo_em.add_field(name = "Stock:", value = stock, inline = False)
                iteminfo_em.add_field(name = "Roles Required:", value = roles_required2, inline = False)
                



                await ctx.send(embed = iteminfo_em)
                return

    no_item_found = discord.Embed(
        title = "No item was found!",
        color = discord.Color.red()
    )
    no_item_found.set_footer(text = "Try checking your spelling!")
    await ctx.send(embed = no_item_found)


"""
Moderator and Admin 
"""


    
    

"""
    Async Functions
"""

async def get_user_data():
    with open("users.json", "r") as f:
        users = json.load(f)

    return users

async def get_userids():
    with open("userids.json","r") as f:
        userids = json.load(f)
    return userids

async def get_store():
    with open("store.json","r") as f:
        store = json.load(f)
    return store


@client.event
async def on_ready():
    print("Ready")
    await client.change_presence(activity=discord.Game(name="In Development"))

@client.command()
async def clearconsole(ctx):
    print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")



client.run(token)
































"""@client.command()
async def displayrawdata(ctx):
    users = await get_user_data()
    userids = await get_userids()

    for id in userids["userids"]:
        for chars in users[id]:
            print(chars)
            for user_info in userids["user_info"]:
                print(users[id][chars][user_info])

@client.command()
async def weapon(ctx):
    users = await get_user_data()
    userids = await get_userids()

    for id in userids["userids"]:
        for chars in users[id]:
            print(chars)
            for weapon in users[id][chars]["weapons"]:
                print(weapon)
            
@client.command()
async def hedge(ctx):
    users = await get_user_data()

    print("Hello")
    users["583610940264546310"]["Hello"] = {}
    users["583610940264546310"]["Hello"]["money"] = 2000000

    with open("users.json", "w") as f:
        json.dump(users,f,sort_keys=True, indent=4, separators=(',', ': '))"""
