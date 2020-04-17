using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class SceneLoader : MonoBehaviour
{
    #region Singleton
    public static SceneLoader Instance = null;

    private void Awake()
    {
        if (Instance == null)
        {
            Instance = this;
        }
    }
    #endregion

    [SerializeField] string[] sceneNames;
    [SerializeField] string currentLoadedScene;

    void Start()
    {
        
    }

    private void Update()
    {
        if (Input.GetKeyDown(KeyCode.A)) {
            LoadScene(0);
        }
    }

    public void LoadScene(int idx) {
        SceneManager.LoadScene(sceneNames[idx], LoadSceneMode.Additive);
        currentLoadedScene = sceneNames[idx];
    }

    void UnloadScene(int idx)
    {

    }

    public void UnloadCurrentScene() {

    }

    public int GetNumberOfTemplate() {
        return sceneNames.Length;
    } 
}
