using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Audio;
using Microsoft.Xna.Framework.Content;
using Microsoft.Xna.Framework.GamerServices;
using Microsoft.Xna.Framework.Graphics;
using Microsoft.Xna.Framework.Input;
using Microsoft.Xna.Framework.Media;

namespace MyTowerDefence
{
    [Serializable]
    public class Menu
    {
        public GameState gamestate { get; set; }
        [NonSerialized]
        private List<StaticTower> towers;
        [NonSerialized]
        private List<MenuButton> buttons;
        [NonSerialized]
        private List<StaticSprite> background;
        public int money { get; set; }
        private int enemycount;
        public int EnemyCount { get { return enemycount; } }
        [NonSerialized]
        private StaticTower towerinfo;

        public Menu(List<StaticTower> towers, List<MenuButton> buttons, List<StaticSprite> background)
        {
            this.towers = new List<StaticTower>(towers);
            this.buttons = new List<MenuButton>(buttons);
            this.background =new List<StaticSprite>(background);
            gamestate = GameState.Paused;
        }

        public void Reload(List<StaticTower> towers, List<MenuButton> buttons, List<StaticSprite> background)
        {
            this.towers = new List<StaticTower>(towers);
            this.buttons = new List<MenuButton>(buttons);
            this.background =new List<StaticSprite>(background);
        }

        public void Draw(SpriteBatch spriteBatch,SpriteFont font)
        {
            foreach (var tow in towers)
                tow.Draw(spriteBatch);
            foreach (var but in buttons)
                but.Draw(spriteBatch);
            foreach (var backgr in background)
                backgr.Draw(spriteBatch);
            if (towerinfo != null)
            {
                spriteBatch.DrawString(font, "Attack radius: " + towerinfo.attackradius.ToString(), new Vector2(495, 110), Color.White, 0, Vector2.Zero, 1, SpriteEffects.None, 1);
                spriteBatch.DrawString(font, "enemy damage: " + towerinfo.bulldamage.ToString(), new Vector2(495, 130), Color.White, 0, Vector2.Zero, 1, SpriteEffects.None, 1);
                spriteBatch.DrawString(font, "Cost: " + towerinfo.cost.ToString(), new Vector2(495, 150), Color.White, 0, Vector2.Zero, 1, SpriteEffects.None, 1);

            }
            if(gamestate==GameState.Started||gamestate==GameState.Paused)
                spriteBatch.DrawString(font, "Enemies to spawn: "+enemycount.ToString(), new Vector2(495, 70), Color.White, 0, Vector2.Zero, 1, SpriteEffects.None, 1);
            else if(gamestate==GameState.GameOver)
                spriteBatch.DrawString(font, "GameOver ", new Vector2(495, 70), Color.White, 0, Vector2.Zero, 1, SpriteEffects.None, 1);
            else if(gamestate==GameState.PlayerWon)
                spriteBatch.DrawString(font, "You Won ", new Vector2(495, 70), Color.White, 0, Vector2.Zero, 1, SpriteEffects.None, 1);
            spriteBatch.DrawString(font, "Money: " + money.ToString(), new Vector2(495, 90), Color.White, 0, Vector2.Zero,1, SpriteEffects.None, 1);
        }

        public void ChooseItem(float x, float y,UserControlledSprite player)
        {
            towerinfo = null;
            foreach (var tow in towers)
                if (tow.BelongToSprite(x, y))
                {
                    if (tow.cost <= money)
                    {
                        money -= tow.cost;
                        player.image=tow.textureimage;
                        player.curtower=tow.towertype;
                        player.towerischosen = true;
                        //(tow.textureimage, tow.Position, new Vector2(6, 6), 0) { curtower = tow.towertype };
                    }
                }
            foreach (var opt in buttons)
                if (opt.BelongToSprite(x, y))
                {
                    gamestate = opt.state;
                    player.towerischosen = false;
                }
        }

        public void ShowInfo(float x, float y)
        {

            foreach (var tow in towers)
                if (tow.BelongToSprite(x, y))
                {
                    towerinfo = tow;
                    break;
                }
        }

        public void Update(int bonusmoney, int enemycount)
        {
            this.money +=bonusmoney;
            this.enemycount = enemycount;
        }
    }
}
