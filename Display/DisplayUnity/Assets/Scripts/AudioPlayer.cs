using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class AudioPlayer : MonoBehaviour
{
    #region Singleton
    public static AudioPlayer Instance = null;

    private void Awake()
    {
        if (Instance == null)
        {
            Instance = this;
        }
    }
    #endregion

    [SerializeField] AudioSource SFX;
    [SerializeField] AudioClip[] clips;
    public void PlaySent() {
        SFX.clip = clips[0];
        SFX.Play();
    }
}
