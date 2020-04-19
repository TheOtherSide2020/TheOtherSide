using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class TokenController : MonoBehaviour
{
    #region Singleton
    public static TokenController Instance = null;

    private void Awake()
    {
        if (Instance == null)
        {
            Instance = this;
        }
    }
    #endregion
    [SerializeField] TokenGenerator[] generators;

    void Start()
    {
        generators = GetComponentsInChildren<TokenGenerator>();
    }

    public void GenerateToken(int idx) {
        generators[idx].GenerateNewToken();
    }
}
