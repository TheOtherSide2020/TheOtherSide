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
    [SerializeField] string currentLoadedScene = "";

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
        if (!currentLoadedScene.Equals(""))
        {
            // unload previous content
            StartCoroutine(UnloadCurrentScene(idx));
        }
        else
        {
            // load new scene
            SceneManager.LoadScene(sceneNames[idx], LoadSceneMode.Additive);
            currentLoadedScene = sceneNames[idx];
        }  
    }

    IEnumerator UnloadCurrentScene(int idx)
    {
        AsyncOperation ao = SceneManager.UnloadSceneAsync(currentLoadedScene);
        yield return ao;
        // load new scene
        SceneManager.LoadScene(sceneNames[idx], LoadSceneMode.Additive);
        currentLoadedScene = sceneNames[idx];
    }

    public int GetNumberOfTemplate() {
        return sceneNames.Length;
    } 
}
