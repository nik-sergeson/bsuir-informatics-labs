using System;
using System.Collections.Generic;
using System.Linq;
using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Audio;
using Microsoft.Xna.Framework.Content;
using Microsoft.Xna.Framework.GamerServices;
using Microsoft.Xna.Framework.Graphics;
using Microsoft.Xna.Framework.Input;
using Microsoft.Xna.Framework.Media;
using System.Runtime.Serialization.Formatters.Binary;
using System.Runtime.Serialization;
using System.IO;

namespace MyTowerDefence
{
    [Serializable]
    public class Building : Sprite
    {
        protected int wrecharge;
        protected int attackradius;
        protected int bullattackradius;
        protected int bulldamage;
        protected int bullmaxspeed;
        protected string texturepath;
        protected string btextpath;
        [NonSerialized]
        private List<Bullet> struckbullets;
        [NonSerialized]
        private Texture2D bullettext;

        public override Vector2 direction
        {
            get { return Vector2.Zero; }
        }

        public void UpdateTexture(Game game)
        {
            textureImage = game.Content.Load<Texture2D>(texturepath);
            bullettext = game.Content.Load<Texture2D>(btextpath);
            struckbullets = new List<Bullet>();
        }

        public override void Update(GameTime gameTime)
        {
            if(wrecharge>0)
                wrecharge -= gameTime.ElapsedGameTime.Milliseconds;
            for (int i = 0; i < struckbullets.Count; i++)
            {
                struckbullets[i].Update(gameTime);
                if (struckbullets[i].Hit() == true)
                {
                    struckbullets[i].HitEnemy();
                    struckbullets.RemoveAt(i);
                }
                if (i<struckbullets.Count&&struckbullets[i] != null)
                {
                    if (Math.Pow(position.X - struckbullets[i].Position.X, 2.0) + Math.Pow(position.Y - struckbullets[i].Position.Y, 2.0) > Math.Pow(bullattackradius, 2.0))
                        struckbullets.RemoveAt(i);
                }
            }
            base.Update(gameTime);
        }

        public override void Draw(SpriteBatch spriteBatch)
        {
            foreach (var bul in struckbullets)
                bul.Draw( spriteBatch);
            base.Draw(spriteBatch);
        }

        public Building(Texture2D textureImage, Texture2D bullettext, float X, float Y, float layerdepth,string texturepath,string bullettextpath)
            : base(textureImage, new Vector2(X - textureImage.Width / 2, Y - textureImage.Height / 2), Vector2.Zero,layerdepth)
        {
            this.texturepath = texturepath;
            this.btextpath = bullettextpath;
            this.bullettext = bullettext;
            ResetCharge();
            struckbullets = new List<Bullet>();
        }

        private void ResetCharge()
        {
            wrecharge = 2000;
        }

        public void Attack(List<Enemy> enemies)
        {
            Vector2 traject;
            if (wrecharge <= 0)
            {
                foreach (var enemy in enemies)
                {
                    if ((Math.Pow(position.X - enemy.Position.X, 2.0) + Math.Pow(position.Y - enemy.Position.Y, 2.0)) <= Math.Pow(attackradius, 2.0))
                    {
                        traject = Bullet.TrajectoryCalculation(enemy, bullmaxspeed, position, new Rectangle((int)(position.X-bullettext.Width/2),(int)(position.Y-bullettext.Height),bullettext.Width,bullettext.Height),bullattackradius);
                        if (traject != Vector2.Zero)
                        {
                            struckbullets.Add(new Bullet(bullettext, position, traject, enemy, bulldamage, (float)0.1));
                            ResetCharge();
                            break;
                        }
                    }
                }
            }
        }
    }
}
